from django.urls import path
from . import views

urlpatterns = [
    path('', views.share_input, name='share_input'),
]