from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from apps.hospitais.models import Hospital

class Funcionario(models.Model):

    nome = models.CharField(
        max_length=100
    )

    cargo = models.CharField(
        max_length=50
    )

    salario = models.FloatField()

    hospital = models.ForeignKey(Hospital, on_delete=DO_NOTHING)