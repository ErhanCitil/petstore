from django.urls import path, include
from rest_framework import routers
from .views import PetViewSet

router = routers.DefaultRouter()
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
