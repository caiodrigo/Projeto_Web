from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculo

def index(request):
    return render(request, 'monitoramento/index.html')

# Página principal do CRUD
def crud_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'monitoramento/crud.html', {'veiculos': veiculos})

# Adicionar um novo veículo
def adicionar_veiculo(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        cor = request.POST['cor']
        Veiculo.objects.create(placa=placa, marca=marca, modelo=modelo, cor=cor)
        return redirect('crud_veiculos')
    return render(request, 'monitoramento/adicionar.html')

# Atualizar veículo existente
def atualizar_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    if request.method == 'POST':
        veiculo.placa = request.POST['placa']
        veiculo.marca = request.POST['marca']
        veiculo.modelo = request.POST['modelo']
        veiculo.cor = request.POST['cor']
        veiculo.save()
        return redirect('crud_veiculos')
    return render(request, 'monitoramento/atualizar.html', {'veiculo': veiculo})

# Excluir um veículo
def excluir_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    veiculo.delete()
    return redirect('crud_veiculos')