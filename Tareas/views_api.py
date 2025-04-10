from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Tarea, Usuario
from .serializers import TareaSerializer, UsuarioSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Schema for registration request
registration_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['username', 'password', 'password2', 'email', 'first_name', 'last_name'],
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de usuario'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña'),
        'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Confirmar contraseña'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='Correo electrónico'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Apellido'),
    }
)

# Schema for login request
login_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['username', 'password'],
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de usuario'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña'),
    }
)

@swagger_auto_schema(
    method='post',
    request_body=registration_schema,
    responses={
        201: openapi.Response('Usuario registrado exitosamente', UserRegistrationSerializer),
        400: 'Datos de registro inválidos'
    },
    operation_description="Registra un nuevo usuario en el sistema"
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserRegistrationSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        request_body=login_schema,
        responses={
            200: openapi.Response('Login exitoso', openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access': openapi.Schema(type=openapi.TYPE_STRING, description='Token de acceso'),
                    'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Token de actualización'),
                    'user': openapi.Schema(type=openapi.TYPE_OBJECT, description='Datos del usuario')
                }
            )),
            401: 'Credenciales inválidas'
        },
        operation_description="Obtiene tokens de acceso y actualización para un usuario"
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = User.objects.get(username=request.data['username'])
            response.data['user'] = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        return response

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @swagger_auto_schema(
        responses={
            200: 'Tarea actualizada exitosamente',
            404: 'Tarea no encontrada'
        },
        operation_description="Cambia el estado de completada de una tarea"
    )
    @action(detail=True, methods=['post'])
    def toggle_completada(self, request, pk=None):
        tarea = self.get_object()
        tarea.completada = not tarea.completada
        tarea.save()
        return Response({'status': 'tarea actualizada', 'completada': tarea.completada})

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Usuario.objects.filter(email=self.request.user.email) 