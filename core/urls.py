from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar-alvo/', views.adicionar_alvo, name='adiciona-alvo'),
    path('editar-alvo/<int:pk>', views.edita_alvo, name='edita-alvo'),
    path('delete-alvo/<int:pk>', views.delete_alvo, name='deleta-alvo'),
    path('mapa/', views.mapa, name='mapa')
]