from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path(r'development/', views.but, name='but'),
    path(r'mobileDev/', views.mob, name='mob'),
    path(r'branding/', views.brand, name='brand'),
]
