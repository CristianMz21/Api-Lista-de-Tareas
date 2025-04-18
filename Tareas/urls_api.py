from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views_api import (
    TareaViewSet, 
    UsuarioViewSet, 
    register_user, 
    CustomTokenObtainPairView
)
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API de Lista de Tareas",
      default_version='v1',
      description="API para gestionar tareas y usuarios",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@tareas.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    # Documentation URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # API URLs
    path('', include(router.urls)),
    path('auth/register/', register_user, name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 