from django.db import models
from django.db.models.deletion import DO_NOTHING
from apps.funcionarios.models import Funcionario
from apps.exames.models import ExameModel
from apps.pacientes.models import Paciente

class ConsultaModel(models.Model):

    data = models.DateTimeField()

    exames = models.ManyToManyField(ExameModel)

    paciente = models.ForeignKey(Paciente, on_delete=DO_NOTHING)

    medicos = models.ForeignKey(Funcionario, on_delete=DO_NOTHING)