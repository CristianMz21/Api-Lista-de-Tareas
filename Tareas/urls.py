from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    TareaListView,
    TareaCreateView,
    TareaUpdateView,
    TareaDeleteView,
    CustomLoginView,
    RegisterView,
    toggle_completada,
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', TareaListView.as_view(), name='tarea_list'),
    path('crear/', TareaCreateView.as_view(), name='tarea_create'),
    path('editar/<int:pk>/', TareaUpdateView.as_view(), name='tarea_update'),
    path('eliminar/<int:pk>/', TareaDeleteView.as_view(), name='tarea_delete'),
    path('toggle-completada/<int:pk>/', toggle_completada, name='toggle_completada'),
]