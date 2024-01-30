from django.urls import path
from .views import list_task, create_task, update_task, delete_task, register

urlpatterns = [
    path('', list_task, name='list_task'),
    path('create/', create_task, name='create_task'),
    path('update/<int:pk>/', update_task, name='update_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('register/', register, name='register')
]
