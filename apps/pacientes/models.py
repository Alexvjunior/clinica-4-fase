from django.db import models

class Paciente(models.Model):

    nome = models.CharField(
        max_length=100
    )

    data_nascimento = models.DateField()

    cpf = models.CharField(
        max_length=15, 
        unique=True
    )