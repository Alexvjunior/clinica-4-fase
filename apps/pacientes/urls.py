from django.urls import path, include
from rest_framework import routers
from .views import PacienteView

app_name="pacientes"

router = routers.SimpleRouter()
router.register("pacientes", PacienteView)

urlpatterns = [
    path('', include(router.urls)),
]