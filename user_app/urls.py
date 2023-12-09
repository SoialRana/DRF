from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from .import views

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    # amra jokhonoi postman software e username and password diye 
    # login korbo tokhoinoi ekta token create create hobe 
    path('register/',views.RegistrationView.as_view(),name='register'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
]