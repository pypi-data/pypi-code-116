import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import update_last_login
from django.contrib.auth.signals import user_logged_in
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View

from nautobot.utilities.forms import ConfirmationForm
from .forms import LoginForm, PasswordChangeForm, TokenForm
from .models import Token


#
# Login/logout
#


class LoginView(View):
    """
    Perform user authentication via the web UI.
    """

    template_name = "login.html"

    @method_decorator(sensitive_post_parameters("password"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        form = LoginForm(request)

        if request.user.is_authenticated:
            logger = logging.getLogger("nautobot.auth.login")
            return self.redirect_to_next(request, logger)

        return render(
            request,
            self.template_name,
            {
                "form": form,
            },
        )

    def post(self, request):
        logger = logging.getLogger("nautobot.auth.login")
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            logger.debug("Login form validation was successful")

            # If maintenance mode is enabled, assume the database is read-only, and disable updating the user's
            # last_login time upon authentication.
            if settings.MAINTENANCE_MODE:
                logger.warning("Maintenance mode enabled: disabling update of most recent login time")
                user_logged_in.disconnect(update_last_login, dispatch_uid="update_last_login")

            # Authenticate user
            auth_login(request, form.get_user())
            logger.info(f"User {request.user} successfully authenticated")
            messages.info(request, "Logged in as {}.".format(request.user))

            return self.redirect_to_next(request, logger)

        else:
            logger.debug("Login form validation failed")

        return render(
            request,
            self.template_name,
            {
                "form": form,
            },
        )

    def redirect_to_next(self, request, logger):
        if request.method == "POST":
            redirect_to = request.POST.get("next", reverse("home"))
        else:
            redirect_to = request.GET.get("next", reverse("home"))

        if redirect_to and not is_safe_url(url=redirect_to, allowed_hosts=request.get_host()):
            logger.warning(f"Ignoring unsafe 'next' URL passed to login form: {redirect_to}")
            redirect_to = reverse("home")

        logger.debug(f"Redirecting user to {redirect_to}")
        return HttpResponseRedirect(redirect_to)


class LogoutView(View):
    """
    Deauthenticate a web user.
    """

    def get(self, request):
        logger = logging.getLogger("nautobot.auth.logout")

        # Log out the user
        username = request.user
        auth_logout(request)
        logger.info(f"User {username} has logged out")
        messages.info(request, "You have logged out.")

        # Delete session key cookie (if set) upon logout
        response = HttpResponseRedirect(reverse("home"))
        response.delete_cookie("session_key")

        return response


#
# User profiles
#


class ProfileView(LoginRequiredMixin, View):
    template_name = "users/profile.html"

    def get(self, request):

        return render(
            request,
            self.template_name,
            {
                "active_tab": "profile",
            },
        )


class UserConfigView(LoginRequiredMixin, View):
    template_name = "users/preferences.html"

    def get(self, request):

        return render(
            request,
            self.template_name,
            {
                "preferences": request.user.all_config(),
                "active_tab": "preferences",
            },
        )

    def post(self, request):
        user = request.user
        data = user.all_config()

        # Delete selected preferences
        for key in request.POST.getlist("pk"):
            if key in data:
                user.clear_config(key)
        user.save()
        messages.success(request, "Your preferences have been updated.")

        return redirect("user:preferences")


class ChangePasswordView(LoginRequiredMixin, View):
    template_name = "users/change_password.html"

    def get(self, request):
        # LDAP users cannot change their password here
        if getattr(request.user, "ldap_username", None):
            messages.warning(
                request,
                "LDAP-authenticated user credentials cannot be changed within Nautobot.",
            )
            return redirect("user:profile")

        form = PasswordChangeForm(user=request.user)

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "active_tab": "change_password",
            },
        )

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has been changed successfully.")
            return redirect("user:profile")

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "active_tab": "change_password",
            },
        )


#
# API tokens
#


class TokenListView(LoginRequiredMixin, View):
    def get(self, request):

        tokens = Token.objects.filter(user=request.user)

        return render(
            request,
            "users/api_tokens.html",
            {
                "tokens": tokens,
                "active_tab": "api_tokens",
            },
        )


class TokenEditView(LoginRequiredMixin, View):
    def get(self, request, pk=None):

        if pk is not None:
            if not request.user.has_perm("users.change_token"):
                return HttpResponseForbidden()
            token = get_object_or_404(Token.objects.filter(user=request.user), pk=pk)
        else:
            if not request.user.has_perm("users.add_token"):
                return HttpResponseForbidden()
            token = Token(user=request.user)

        form = TokenForm(instance=token)

        return render(
            request,
            "generic/object_edit.html",
            {
                "obj": token,
                "obj_type": token._meta.verbose_name,
                "form": form,
                "return_url": reverse("user:token_list"),
                "editing": token.present_in_database,
            },
        )

    def post(self, request, pk=None):

        if pk is not None:
            token = get_object_or_404(Token.objects.filter(user=request.user), pk=pk)
            form = TokenForm(request.POST, instance=token)
        else:
            token = Token()
            form = TokenForm(request.POST)

        if form.is_valid():
            token = form.save(commit=False)
            token.user = request.user
            token.save()

            msg = "Modified token {}".format(token) if pk else "Created token {}".format(token)
            messages.success(request, msg)

            if "_addanother" in request.POST:
                return redirect(request.path)
            else:
                return redirect("user:token_list")

        return render(
            request,
            "generic/object_edit.html",
            {
                "obj": token,
                "obj_type": token._meta.verbose_name,
                "form": form,
                "return_url": reverse("user:token_list"),
                "editing": token.present_in_database,
            },
        )


class TokenDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):

        token = get_object_or_404(Token.objects.filter(user=request.user), pk=pk)
        initial_data = {
            "return_url": reverse("user:token_list"),
        }
        form = ConfirmationForm(initial=initial_data)

        return render(
            request,
            "generic/object_delete.html",
            {
                "obj": token,
                "obj_type": token._meta.verbose_name,
                "form": form,
                "return_url": reverse("user:token_list"),
            },
        )

    def post(self, request, pk):

        token = get_object_or_404(Token.objects.filter(user=request.user), pk=pk)
        form = ConfirmationForm(request.POST)
        if form.is_valid():
            token.delete()
            messages.success(request, "Token deleted")
            return redirect("user:token_list")

        return render(
            request,
            "generic/object_delete.html",
            {
                "obj": token,
                "obj_type": token._meta.verbose_name,
                "form": form,
                "return_url": reverse("user:token_list"),
            },
        )
