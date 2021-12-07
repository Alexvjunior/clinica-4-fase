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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = FuncionariosRetrieveSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = FuncionariosRetrieveSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FuncionariosRetrieveSerializer(instance)
        return Response(serializer.data)
