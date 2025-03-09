from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Главная страница
    path('about/', views.about, name='about'),  # О проекте
    path('tips/', views.tips, name='tips'),  # Советы по уходу
    path('plants/', views.plants, name='plants'),  # Новая страница с растениями
]