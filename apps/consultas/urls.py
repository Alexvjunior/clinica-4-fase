from django.urls import path, include
from rest_framework import routers
from .views import ConsultaView

app_name="consultas"

router = routers.SimpleRouter()
router.register("consultas", ConsultaView)

urlpatterns = [
    path('', include(router.urls)),
]