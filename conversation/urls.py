from django.urls import path
from conversation import views

app_name='conversation'

urlpatterns = [
    path('new/<int:pdf_pk>/',views.new_conversation,name='new'),
]
