from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('',views.home,name='base'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf')
]
