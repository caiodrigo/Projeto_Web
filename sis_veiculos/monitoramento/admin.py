from django.contrib import admin
from .models import Veiculo, Motorista, Vaga, EntradaSaida

admin.site.register(Veiculo)
admin.site.register(Motorista)
admin.site.register(Vaga)
admin.site.register(EntradaSaida)
