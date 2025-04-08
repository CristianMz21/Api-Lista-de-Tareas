from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Tarea
from .forms import TareaForm

class TareaListView(ListView):
    model = Tarea
    template_name = 'tarea_list.html'  
    context_object_name = 'tareas'

    def get_queryset(self):
        return Tarea.objects.all().order_by('-fecha_creacion')

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tarea_list')
