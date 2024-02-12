from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import SignInForm


app_name = 'users'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='logout'),
    # path("logout/", auth_views.LogoutView.as_view(next_page='users:signin'), name="logout")
]