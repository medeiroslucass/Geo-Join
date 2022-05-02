from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar-alvo/', views.adicionar_alvo, name='adiciona-alvo'),
    path('mapa/', views.mapa, name='mapa')
]