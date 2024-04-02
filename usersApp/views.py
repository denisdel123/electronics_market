from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView

from config.settings import ADDRESS_MAIL_RU
from usersApp.forms import UserForm, UserUpdateForm
from usersApp.models import User


class LoginView(BaseLoginView):
    template_name = 'usersApp/login.html'


class LogoutView(BaseLogoutView):
    pass


class UserDetailView(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user


class RegistrationView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('usersApp:login')
    template_name = 'usersApp/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Регистрация на сайте',
            message='Поздравляю вы зарегистрировались на сайте магазина электроники',
            from_email=ADDRESS_MAIL_RU,
            recipient_list=[new_user],
        )
        return super().form_valid(form)





class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('usersApp:user_detail')
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
