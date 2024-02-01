from django.urls import path
from . import views
from django.views.generic.base import TemplateView  # new
app_name = 'base'
urlpatterns = [
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('view_pdf/', views.view_pdf, name='view_pdf'),

]
