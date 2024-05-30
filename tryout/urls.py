from django.urls import path
from . import views

urlpatterns = [
    path('api/tryout/new', views.create_tryout, name='create_tryout'),
]
