from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import UserProfileSerializer, EmailLoginSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from .authentication import EmailAuthenticationBackend
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class RegisterUserView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        if CustomUser.objects.filter(email=request.data.get('email')).exists():
            return Response(
                {'error': 'Указанный адрес электронной почты уже зарегистрирован!'},
                status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()


class UserLoginView(generics.GenericAPIView):
    serializer_class = EmailLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = EmailAuthenticationBackend.authenticate(request, username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'refresh': str(refresh),
                'access': access_token
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Неправильный email или пароль'}, status=status.HTTP_401_UNAUTHORIZED)