from django.urls import path
from . import views

urlpatterns = [
    path('api/tryout/health', views.health_check, name='health_check'),
    path('api/tryout/new', views.create_tryout, name='create_tryout'),
    path('api/tryout/data', views.get_tryout, name='get_tryout'),
]
