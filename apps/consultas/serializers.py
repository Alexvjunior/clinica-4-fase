from rest_framework import serializers

from apps.funcionarios.serializers import FuncionariosViewSerializer
from .models import ConsultaModel
from apps.exames.serializers import ExamesViewSerializer
from apps.pacientes.serializers import PacientesSerializer

class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsultaModel
        fields = ("id", "data", "exames", "paciente", "medicos")

class ConsultaRetrieveSerializer(serializers.ModelSerializer):
    medicos = FuncionariosViewSerializer()
    paciente = PacientesSerializer()
    exames = ExamesViewSerializer(many=True)

    class Meta:
        model = ConsultaModel
        fields = ("id", "data", "exames", "paciente", "medicos")