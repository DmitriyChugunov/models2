
from django.urls import path, include

from .views import index, create, update, delete

urlpatterns = [
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
    path('create', create, name='create'),
    path('', index, name='home')
]
