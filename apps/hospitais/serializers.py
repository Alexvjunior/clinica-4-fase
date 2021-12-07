from rest_framework import serializers
from .models import Hospital

class HospitaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ("id", "nome")