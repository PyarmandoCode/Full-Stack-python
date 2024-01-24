from django.urls import path
from .views import index,quienes,portafolio

urlpatterns = [
    path('', index),
    path('quienes/', quienes),
    path('portafolio/', portafolio),
]