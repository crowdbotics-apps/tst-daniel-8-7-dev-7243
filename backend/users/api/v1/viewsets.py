from rest_framework import authentication
from users.models import GHjhg, HGFJHf, JHGHFjg
from .serializers import GHjhgSerializer, HGFJHfSerializer, JHGHFjgSerializer
from rest_framework import viewsets


class JHGHFjgViewSet(viewsets.ModelViewSet):
    serializer_class = JHGHFjgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = JHGHFjg.objects.all()


class HGFJHfViewSet(viewsets.ModelViewSet):
    serializer_class = HGFJHfSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = HGFJHf.objects.all()


class GHjhgViewSet(viewsets.ModelViewSet):
    serializer_class = GHjhgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = GHjhg.objects.all()
