from rest_framework import viewsets
from rest_framework import authentication
from .serializers import (
    CustomTextSerializer,
    Fftrghy64rjrSerializer,
    GtjguySerializer,
    HHHhgfhfhgfSerializer,
    HomePageSerializer,
    JHGJGJGSerializer,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    CustomTextSerializer,
    HomePageSerializer,
    UserSerializer,
)
from home.models import CustomText, Fftrghy64rjr, Gtjguy, HHHhgfhfhgf, HomePage, JHGJGJG


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class CustomTextViewSet(ModelViewSet):
    serializer_class = CustomTextSerializer
    queryset = CustomText.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class HomePageViewSet(ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class HHHhgfhfhgfViewSet(viewsets.ModelViewSet):
    serializer_class = HHHhgfhfhgfSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = HHHhgfhfhgf.objects.all()


class JHGJGJGViewSet(viewsets.ModelViewSet):
    serializer_class = JHGJGJGSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = JHGJGJG.objects.all()


class GtjguyViewSet(viewsets.ModelViewSet):
    serializer_class = GtjguySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Gtjguy.objects.all()


class Fftrghy64rjrViewSet(viewsets.ModelViewSet):
    serializer_class = Fftrghy64rjrSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Fftrghy64rjr.objects.all()
