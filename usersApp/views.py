from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView

from config.settings import ADDRESS_MAIL_RU
from usersApp.forms import UserForm, UserUpdateForm
from usersApp.models import User
from usersApp.utils import recovery_password


class LoginView(BaseLoginView):
    template_name = 'usersApp/login.html'


class LogoutView(BaseLogoutView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
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
        try:
            send_mail(
                subject='Регистрация на сайте',
                message='Поздравляю вы зарегистрировались на сайте магазина электроники',
                from_email=ADDRESS_MAIL_RU,
                recipient_list=[new_user],
            )
            new_user.is_active = True
        except Exception:
            pass

        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('usersApp:user_detail')
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

@login_required
def generate_new_password(request):
    password = get_random_string(12)
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль {password}',
        from_email=ADDRESS_MAIL_RU,
        recipient_list=[request.user.email]
    )
    request.user.set_password(password)
    request.user.save()
    return redirect(reverse_lazy('marketApp:category_list'))


def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        answer = recovery_password(email)

        if len(answer) == 2:
            return render(request, answer['success'], answer['context'])
        elif len(answer) == 1:
            return render(request, answer['success'])


class UserListView(LoginRequiredMixin, ListView):
    model = User


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('marketApp:main')
