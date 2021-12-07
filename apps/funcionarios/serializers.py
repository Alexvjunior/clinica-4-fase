from rest_framework import serializers

from apps.hospitais.serializers import HospitaisSerializer
from .models import Funcionario

class FuncionariosCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcionario
        fields = ("id", "nome", "salario", "cargo", "hospital")

class FuncionariosRetrieveSerializer(serializers.ModelSerializer):
    hospital = HospitaisSerializer()

    class Meta:
        model = Funcionario
        fields = ("id", "nome", "salario", "cargo", "hospital")