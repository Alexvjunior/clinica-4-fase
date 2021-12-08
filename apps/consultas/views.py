from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ConsultaRetrieveSerializer, ConsultaSerializer
from .models import ConsultaModel

class ConsultaView(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = ConsultaModel.objects.all()
    http_method_names = [
        'post',
        'get',
        'patch',
        'delete',
    ]   

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ConsultaRetrieveSerializer(instance)
        return Response(serializer.data)
