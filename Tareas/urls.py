from django.urls import path

from .views import TareaListView, TareaDetailView, TareaCreateView, TareaUpdateView, TareaDeleteView

urlpatterns = [
    path('', TareaListView.as_view(), name='tarea-list'),
    path('tarea/<int:pk>/', TareaDetailView.as_view(), name='tarea-detail'),
    path('tarea/nueva/', TareaCreateView.as_view(), name='tarea-create'),
    path('tarea/<int:pk>/editar/', TareaUpdateView.as_view(), name='tarea-update'),
    path('tarea/<int:pk>/eliminar/', TareaDeleteView.as_view(), name='tarea-delete'),
]