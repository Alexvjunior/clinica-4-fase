from django.db import models
from django.db.models.deletion import DO_NOTHING
from apps.funcionarios.models import Funcionario

class ExameModel(models.Model):

    nome = models.CharField(max_length=100)

    descricao = models.CharField(max_length=500)

    medico = models.ForeignKey(Funcionario, on_delete=DO_NOTHING)