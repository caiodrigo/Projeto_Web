from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from datetime import datetime

class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.marca} {self.modelo} -  {self.placa}"


class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    numero = models.PositiveIntegerField(unique=True, blank=True, null=True)
    veiculo = models.OneToOneField(Veiculo, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='vaga')
    motorista =  models.OneToOneField(Motorista, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='vaga')

    def ocupar(self, veiculo: Veiculo, motorista: Motorista):
        self.veiculo = veiculo
        self.motorista = motorista
        self.save()
        return self
    
    def desocupar(self):
        if self.veiculo and self.motorista:
            self.veiculo = None
            self.motorista = None
            self.save()
            return self
        return "Vaga não está ocupada"

    def __str__(self):
        return f"Vaga {self.numero} - {'Ocupada' if self.veiculo else 'Disponivel'}"


class EntradaSaida(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE,)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    entrada = models.DateTimeField(auto_now_add=True)
    saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.veiculo} - Entrada: {self.entrada} - Saída: {self.saida or 'Em andamento'}"




@receiver(post_save, sender=Vaga)
def gerar_numero_vaga(sender, instance, created, **kwargs):
    if created:
        data = datetime.now()
        numero = f"{data.year}{data.month}{data.day}0{data.second}"
        instance.numero = int(numero)
        instance.save()

post_save.connect(gerar_numero_vaga, sender=Vaga)