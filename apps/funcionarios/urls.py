from django.urls import path, include
from rest_framework import routers
from .views import FuncionarioView

app_name="funcionarios"

router = routers.SimpleRouter()
router.register("funcionarios", FuncionarioView)

urlpatterns = [
    path('', include(router.urls)),
]