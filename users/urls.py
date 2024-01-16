from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import SignInForm


app_name = 'users'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',auth_views.LoginView.as_view(template_name='users/signin.html',authentication_form=SignInForm),name='signin'),
    path('signout/', auth_views.LogoutView.as_view(http_method_names=['post']),name='signout'),
# template_name='users/signout.html'

]