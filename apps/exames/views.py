from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ExamesSerializer, ExamesRetrieveSerializer
from .models import ExameModel

class ExameView(viewsets.ModelViewSet):
    serializer_class = ExamesSerializer
    queryset = ExameModel.objects.all()
    http_method_names = [
        'post',
        'get',
        'patch',
        'delete',
    ]   

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ExamesRetrieveSerializer(instance)
        return Response(serializer.data)
