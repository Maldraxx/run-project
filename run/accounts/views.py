from constants import POST, SWAGGER_ACCOUNTS_TAG
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

from .Account import Account
from .serializers import (AccountCreationSerializer, LoginSerializer,
                          UserSerializer)


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    obj_account = Account()

    @swagger_auto_schema(request_body=LoginSerializer, tags=[SWAGGER_ACCOUNTS_TAG])
    @action(detail=False, methods=[POST])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        return self.obj_account.login(email, password)

    @swagger_auto_schema(request_body=AccountCreationSerializer, tags=[SWAGGER_ACCOUNTS_TAG])
    @action(detail=False, methods=[POST])
    def account_creation(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        location = request.data.get('location')
        
        return self.obj_account.account_creation(email, password, username, location)