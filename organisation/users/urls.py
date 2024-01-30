from django.urls import path
from . import views

#  These files are needed for resetting the password
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path("", views.details, name="details"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.sign_out, name="logout"),
    path("register/", views.register, name="register"),
    path("notes/", views.notes, name="notes"),
    path(
        "password-reset",
        views.password_reset,
        name="password_reset",
    ),
    path(
        "password-reset-done/",
        views.password_reset_done,
        name="password_reset_done_final",
    ),
    # path(
    #     "password-reset-confirm/<uidb64>/<token>",
    #     PasswordResetConfirmView.as_view(
    #         template_name="users/password_reset_confirm.html"
    #     ),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "password-reset-complete/<uidb64>/<token>",
    #     PasswordResetCompleteView.as_view(
    #         template_name="users/password_reset_complete.html"
    #     ),
    #     name="password_reset_complete",
    # ),
]
