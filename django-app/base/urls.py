from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHello, name='hello'),
]