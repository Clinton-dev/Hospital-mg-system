from django.urls import path, include
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('register_admin/', views.registration, name='admin-registration'),
    path('forgot_password/', views.change_password, name='change-password'),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.user_profile, name="profile"),
]
