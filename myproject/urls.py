from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница "О проекте"
    path('tips/', views.tips, name='tips'),  # Страница "Советы по уходу"
]