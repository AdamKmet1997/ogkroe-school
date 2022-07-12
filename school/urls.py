from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('academy/', views.academy, name='academy'),
    path('add/',  views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete_results/<int:id>/', views.delete_results, name='delete_results'),
    path('rules/',  views.rules, name='rules'),
    path('results/',  views.results, name='results'),
    path('history/',  views.history, name='history'),
    path('about/',  views.about, name='about'),
]