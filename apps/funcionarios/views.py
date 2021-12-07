from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FuncionariosCreateSerializer, FuncionariosRetrieveSerializer
from .models import Funcionario

class FuncionarioView(viewsets.ModelViewSet):
    serializer_class = FuncionariosCreateSerializer
    queryset = Funcionario.objects.all()
    http_method_names = [
        'post',
        'get',
        'patch',
        'delete',
    ]   

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FuncionariosRetrieveSerializer(instance)
        return Response(serializer.data)
