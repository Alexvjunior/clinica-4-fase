from rest_framework import serializers

from apps.funcionarios.serializers import FuncionariosViewSerializer
from .models import ExameModel

class ExamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExameModel
        fields = ("id", "nome", "descricao", "medico")

class ExamesRetrieveSerializer(serializers.ModelSerializer):
    medico = FuncionariosViewSerializer()

    class Meta:
        model = ExameModel
        fields = ("id", "nome", "descricao", "medico")

class ExamesViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExameModel
        fields = ("id", "nome", "descricao")