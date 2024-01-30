from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import (
    LoginForm,
    RegisterForm,
    PasswordResetForm,
    PasswordResetDoneForm,
)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import NotesForm
from .models import Notes, CustomUser


from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

# from .views import sign_in, sign_out


# Create your views here.


# Home page
def details(request):
    if request.user.is_authenticated:
        notes = Notes.objects.filter(employee__role=request.user.role)[::-1]
        context = {"notes": notes}
        return render(request, "users/base.html", context)
    return redirect(
        "login"
    )  # the use of name in url is used here because reverse match is not possible so we use redirect here we use the name to go to that page easily


def sign_in(request):
    # pdb.set_trace()
    # this is if the method is get
    if request.method == "GET":
        #  if the user is being logged in before only then he'll directly redirected to the notes, as if we have logged in into the instagram, and haven't logged out, then it will open directly to the home/posts of the instagram
        if request.user.is_authenticated:
            return redirect("notes")

        # else if the user is not logged in then he will be redirected to the login form so that he can login.
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    # this for post method
    elif request.method == "POST":
        # request.POST will send the credentials in secured way

        form = LoginForm(request.POST)

        # is_valid() validates each field of the form, If True if data is valid and place all data into cleaned_data attribute
        if form.is_valid():
            # so if the form is_valid then only it will place the data into the cleaned_data attibute
            # if form.is_valid() then only the value are stored in the fields of form in the form of key:value pair, and if we want to access it out of is_valid then it will make an Attribute Error, that this type of attribute does not exist

            username = form.cleaned_data["username"]

            password = form.cleaned_data["password"]

            # the authenticate checks the username and password, and if both are same as in the database, it then returns an instance(object) of User or None otherwise

            user = authenticate(
                request, username=username, password=password
            )  # this statement will give True or False, boolean value if both are same/authenticated

            # so if user is True, then it will login the user, login() function take HttpRequest object(request) and User object(user), user object saves user's ID in the session, using django's session framework
            if user:
                login(request, user)
                # the message()is a framework which allows us to store the message, and retrieve them in the next upcoming request.(the messages can be debug,success, info, warnning,error )
                messages.success(request, f"Hi {username.title()}, welcome back!")
                return redirect("notes")
            # else
            messages.error(request, f"Invalid username or password.")
            return render(request, "users/login.html", {"form": form})


def sign_out(request):
    # logout doesn't return any value, it just log out the person and erase the existing data, so that if any person comes and want to login then it's possible to do that
    logout(request)
    # it tells the user by sending the message that he's being logged out
    messages.success(request, "You are logged out.")
    # this return the person to the login page, so that one can login.
    return redirect("login")


def register(request):
    if request.method == "GET":
        # if the user sends get request means if wants to go to the sign up form through url then this HttpRequest method will run and he will get the signup form to register

        form = RegisterForm()

        return render(request, "users/register.html", {"form": form})

    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have signed up successfully")
            login(request, user)
            return redirect("notes")

        else:
            return render(request, "users/register.html", {"form": form})


# notes
# in notes, if Http request is GET, then it create a new instance of the NotesForm class and pass it to the render function
def notes(request):
    # same done in registration, we are taking get method, then rendering the notes page, and saving the context in the form from NotesForm

    # if request.user.is_authenticated:
    #         notes = Notes.objects.all()
    #         context = {"notes": notes}
    #         return render(request, "users/base.html", context)
    # return redirect(
    #     "login"
    # )

    if request.user.is_authenticated:
        if request.method == "GET":
            # context is the data passed to the template for rendering
            context = {"form": NotesForm()}
            return render(request, "users/notes.html", context)

        elif request.method == "POST":
            # if the method is post, then we will create the new instance, NotesForm and then check whether the form is valid or not, and if valid then we will save it and redirect it to the notes page, and if not valid then the page will be loaded with the same values and errors, like in any form we forgot to fill any block then it reidrects us to the same page with the old entered values and the errors.
            form = NotesForm(request.POST)

            if form.is_valid():
                notes = form.cleaned_data["notes"]
                Notes.objects.create(notes=notes, employee=request.user)
                return redirect("details")
            else:
                return render(request, "users/notes.html", {"form": form})
    return redirect("login")

    # this is for forgot password reset

    if request.method == "GET":
        context = {"form": SuccessForm()}
        return render(request, "users/success.html", context)

    elif request.method == "POST":
        form = SuccessForm(request.POST)

    return redirect("login")


def password_reset(request):
    if request.method == "GET":
        context = {"form": PasswordResetForm()}
        return render(request, "users/password_reset.html", context)

    elif request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            pet_name = form.cleaned_data["pet_name"]
            try:
                user = CustomUser.objects.get(email=email, pet_name=pet_name)
                uname = user.username
                return redirect(
                    reverse("password_reset_done_final") + f"?username={uname}"
                )

            except:
                return HttpResponse("Invalid email and pet_name")

        return redirect("login")


def password_reset_done(request):
    if request.method == "GET":
        username = request.GET.get("username", "")
        context = {"form": PasswordResetDoneForm(), "username": username}
        return render(request, "users/password_reset_done.html", context)

    elif request.method == "POST":
        form = PasswordResetDoneForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username", "")
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if password1 == password2:
                try:
                    user = CustomUser.objects.get(username=username)
                    user.set_password(password1)
                    user.save()
                except CustomUser.DoesNotExist:
                    return redirect("password_reset")
                return redirect("success")
        return redirect("login")
