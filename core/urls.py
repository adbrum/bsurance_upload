from django.urls import path
from core import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('img/<str:image_name>/', views.show_images, name='show_image'),
]
