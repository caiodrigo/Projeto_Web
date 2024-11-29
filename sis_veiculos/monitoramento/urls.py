from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crud/', views.crud_veiculos, name='crud_veiculos'),
    path('adicionar/', views.adicionar_veiculo, name='adicionar_veiculo'),
    path('atualizar/<int:veiculo_id>/', views.atualizar_veiculo, name='atualizar_veiculo'),
    path('excluir/<int:veiculo_id>/', views.excluir_veiculo, name='excluir_veiculo'),
]