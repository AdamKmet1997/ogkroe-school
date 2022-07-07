from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/',  views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('rules/',  views.rules, name='rules'),
]