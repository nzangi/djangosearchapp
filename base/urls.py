from django.urls import path
from . import views
from django.views.generic.base import TemplateView  # new
app_name = 'base'

urlpatterns = [
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('view_pdf/', views.view_pdf, name='view_pdf'),
    path('view_pdf/<int:pk>/', views.view_pdf_at_time, name='view_pdf_at_time'),
    path('view_pdf/<int:pk>/update_pdf/', views.update_pdf, name='update_pdf'),
    path('delete_pdf/<int:pk>/', views.delete_pdf, name='delete_pdf'),
    path('browser_pdf/<int:pk>/', views.browser_pdf, name='browser_pdf'),
    
]
