from django.shortcuts import render, redirect, get_object_or_404
from .forms import MotoristaForm
from .models import Veiculo, Motorista, Vaga


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


def crud_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'monitoramento/vagas.html', context={
        'vagas': vagas,
    })


def vagas_ocopar(request, numero):
    vaga = get_object_or_404(Vaga, numero=numero)
    error = None

    if request.method == 'POST':
        data = request.POST

        try:
            veiculo = get_object_or_404(Veiculo, id=data.get('veiculo'))

            motorista = get_object_or_404(Motorista, cpf=data.get('cpf'))
            print(motorista)
            vaga.ocupar(veiculo=veiculo, motorista=motorista)

            return redirect(crud_vagas)
        except:
            error = F"Erro ao salvar"
    veiculos = Veiculo.objects.filter(vaga=None)
    return render(request, 'monitoramento/vagas_ocupar.html', {
        'vaga': vaga,
       'veiculos':veiculos,
       'error':error
    })

def vagas_desocupar(request, numero):
    vaga = get_object_or_404(Vaga, numero=numero)
    if request.method =="POST":
        vaga.desocupar()
        return redirect(crud_vagas)

    return render(request, 'monitoramento/vagas_desocupar.html', {
        'vaga': vaga,
    })
    

def vagas_editar(request, numero):
    vaga = get_object_or_404(Vaga, numero=numero)
    error = None

    if request.method == 'POST':
        data = request.POST

        
        vaga.veiculo = veiculo
        vaga.motorista = motorista
        vaga.save()
        return redirect(crud_vagas)
    return render(request, 'monitoramento/vagas_ocupar.html', {
        'vaga': vaga,
       'error':error
    })

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
