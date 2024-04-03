from django.urls import path

from usersApp.apps import UsersappConfig
from usersApp.views import LoginView, LogoutView, RegistrationView, UserDetailView, UserUpdateView, \
    generate_new_password, forget_password, UserListView, UserDeleteView

app_name = UsersappConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('user/generate_password', generate_new_password, name='password_generate'),
    path('forget_password', forget_password, name='forget_password'),

    path('detail', UserDetailView.as_view(), name='user_detail'),
    path('update', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),
    path('users_list', UserListView.as_view(), name='user_list'),

]
