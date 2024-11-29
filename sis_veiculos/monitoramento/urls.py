from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('veiculos/', views.crud_veiculos, name='crud_veiculos'),
    path('veiculos/add/', views.adicionar_veiculo, name='veiculos_add'),
    path('veiculos/edit/<int:veiculo_id>/', views.atualizar_veiculo, name='veiculos_edit'),
    path('veiculos/delete/<int:veiculo_id>/', views.excluir_veiculo, name='veiculos_delete'),
    path('motoristas/', views.crud_motoristas, name='crud_motoristas'),
    path('motoristas/add/', views.motoristas_add, name='motoristas_add'),
    path('motoristas/edit/<int:id>/', views.motoristas_edit, name='motoristas_edit'),
    path('motoristas/delete/<int:id>/', views.motoristas_delete, name='motoristas_delete'),
]