from . import views
from django.urls import path


app_name = 'users'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/', views.signin, name='signin')
]