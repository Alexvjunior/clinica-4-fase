from rest_framework import serializers
from .models import Paciente

class PacientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = ("id", "nome", "data_nascimento", "cpf")