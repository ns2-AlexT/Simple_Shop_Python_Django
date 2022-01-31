from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('user/registration/', authapp.registration, name='registration'),
    path('user/updating/', authapp.updating, name='updating'),
]
