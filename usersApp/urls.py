from django.urls import path

from usersApp.apps import UsersappConfig
from usersApp.views import LoginView, LogoutView, RegistrationView, UserDetailView, UserUpdateView

app_name = UsersappConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('user/detail', UserDetailView.as_view(), name='user_detail'),
    path('user/update', UserUpdateView.as_view(), name='user_update'),

]