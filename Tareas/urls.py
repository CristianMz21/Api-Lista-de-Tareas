from django.urls import path
from .views import TareaListView, TareaCreateView



urlpatterns = [
    path('', TareaListView.as_view(), name='tarea_list'),
    path('crear/', TareaCreateView.as_view(), name='tarea_create'),
]