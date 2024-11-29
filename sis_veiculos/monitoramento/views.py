from django.shortcuts import render, redirect, get_object_or_404
from .forms import MotoristaForm
from .models import Veiculo, Motorista

def index(request):
    return render(request, 'monitoramento/index.html')

# Página principal do CRUD
def crud_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'monitoramento/veiculos.html', {'veiculos': veiculos})

# Adicionar um novo veículo
def adicionar_veiculo(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        cor = request.POST['cor']
        Veiculo.objects.create(placa=placa, marca=marca, modelo=modelo, cor=cor)
        return redirect('crud_veiculos')
    return render(request, 'monitoramento/veiculos_add.html')

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
    return render(request, 'monitoramento/veiculos_edit.html', {'veiculo': veiculo})

# Excluir um veículo
def excluir_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    veiculo.delete()
    return redirect('crud_veiculos')

# Listar motoristas
def crud_motoristas(request):
    motoristas = Motorista.objects.all()
    return render(request, 'monitoramento/motoristas.html', {'motoristas': motoristas})

# Adicionar motorista
def motoristas_add(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_motoristas')
    else:
        form = MotoristaForm()
    return render(request, 'monitoramento/motoristas_add.html', {'form': form})

# Editar motorista
def motoristas_edit(request, id):
    motorista = get_object_or_404(Motorista, id=id)
    if request.method == 'POST':
        form = MotoristaForm(request.POST, instance=motorista)
        if form.is_valid():
            form.save()
            return redirect('crud_motoristas')
    else:
        form = MotoristaForm(instance=motorista)
    return render(request, 'monitoramento/motoristas_edit.html', {'form': form})

# Excluir motorista
def motoristas_delete(request, id):
    motorista = get_object_or_404(Motorista, id=id)
    motorista.delete()
    return redirect('crud_motoristas')
