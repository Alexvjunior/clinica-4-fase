from django.urls import path, include
from rest_framework import routers
from .views import HospitalView

app_name="hospitais"

router = routers.SimpleRouter()
router.register("hospitais", HospitalView)

urlpatterns = [
    path('', include(router.urls)),
]