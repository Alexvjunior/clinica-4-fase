from rest_framework import viewsets
from .serializers import FuncionariosSerializer
from .models import Funcionario

class FuncionarioView(viewsets.ModelViewSet):
    serializer_class = FuncionariosSerializer
    queryset = Funcionario.objects.all()
    http_method_names = [
        'post',
        'get',
        'patch',
        'delete',
    ]   
