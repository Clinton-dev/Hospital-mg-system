from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('register_admin/', views.registration, name='admin-registration'),
    path('forgot_password/', views.change_password, name='change-password'),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.user_profile, name="profile"),
    path('user/<int:pk>/update', views.UsersUpdateView.as_view(template_name='hospital/user_form.html'),
         name='user-update'),
    path('user/<int:pk>/delete', views.UserDeleteView.as_view(template_name='hospital/user_confirm_delete.html'),
         name='user-delete'),
    # reset userpassword
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_change.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_password_complete.html'), name='password_reset_complete'),
]
