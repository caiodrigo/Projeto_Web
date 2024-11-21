from django.shortcuts import render
from .models import Vaga

def index(request):
    vagas = Vaga.objects.all()
    return render(request, 'monitoramento/index.html', {'vagas': vagas})
