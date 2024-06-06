from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.perms import GroupPerms

from users.models import User
from django.contrib.auth.views import PasswordChangeView
from users.forms import CustomUserCreationForm

# Create your views here.
class UserListView(GroupPerms, generic.ListView):
    model = User
    template_name = "registration/user_list.html"
    context_object_name = "user_list"
    queryset = User.objects.all()[:50]
    order="-date_joined"


class CustomUserCreateView(GroupPerms, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "registration/user_form.html"
    success_url = reverse_lazy("transport:list")

    def form_valid(self, form):
        messages.success(self.request, "帳號註冊成功！")
        return super().form_valid(form)


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("custom_password_change")
    template_name = "registration/password_change_form.html"

    def form_valid(self, form):
        messages.success(self.request, "密碼已經成功變更！")
        return super().form_valid(form)


class UserDeleteView(GroupPerms, generic.DeleteView):
    model = User
    template_name = "registration/user_delete.html"
    context_object_name = "user"
    success_url = reverse_lazy("user_list")