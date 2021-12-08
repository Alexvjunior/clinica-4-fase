from rest_framework import viewsets
from .serializers import HospitaisSerializer
from .models import Hospital

class HospitalView(viewsets.ModelViewSet):
    serializer_class = HospitaisSerializer
    queryset = Hospital.objects.all()
    http_method_names = [
        'post',
        'get',
        'patch',
        'delete',
    ]   

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)