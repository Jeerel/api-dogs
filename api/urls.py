from django.urls import path
from .views import DogView

urlpatterns = [
    path('dogs/', DogView.as_view(), name='dog_list'),
    path('dogs/<int:id>', DogView.as_view(), name='dog_process')
]
