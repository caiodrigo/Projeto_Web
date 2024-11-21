from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=30)

    def __str__(self):
        return self.placa

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    status = models.BooleanField(default=True)  # True = Disponível, False = Ocupada

    def __str__(self):
        return f"Vaga {self.numero} - {'Disponível' if self.status else 'Ocupada'}"

class EntradaSaida(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    entrada = models.DateTimeField(auto_now_add=True)
    saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.veiculo} - Entrada: {self.entrada} - Saída: {self.saida or 'Em andamento'}"
