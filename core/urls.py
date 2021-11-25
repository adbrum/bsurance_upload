from django.urls import path
from core import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
]
