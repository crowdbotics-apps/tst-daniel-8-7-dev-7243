from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GHjhgViewSet, HGFJHfViewSet, JHGHFjgViewSet

router = DefaultRouter()
router.register("jhghfjg", JHGHFjgViewSet)
router.register("hgfjhf", HGFJHfViewSet)
router.register("ghjhg", GHjhgViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
