from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PacientesSerializer
from .models import Paciente

class PacienteView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PacientesSerializer
    queryset = Paciente.objects.all()
    http_method_names = [
        'post',
        'get',
        'patch',
        'delete',
    ]   
