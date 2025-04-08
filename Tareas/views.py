from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Tarea
from .forms import TareaForm, UserRegisterForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tarea_list')

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos')
        return super().form_invalid(form)

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('tarea_list')
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tarea_list')
        return super(RegisterView, self).get(*args, **kwargs)

class TareaListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea_list.html'
    context_object_name = 'tareas'
    login_url = 'login'

    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user).order_by('-fecha_creacion')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.utils import timezone
        context['now'] = timezone.now()
        return context

class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tarea_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, 'Tarea creada exitosamente')
        return super().form_valid(form)

class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tarea_list')
    login_url = 'login'

    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Tarea actualizada exitosamente')
        return super().form_valid(form)

class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea_list')
    login_url = 'login'

    def get_queryset(self):
        return self.model.objects.filter(usuario=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Tarea eliminada exitosamente')
        return super().delete(request, *args, **kwargs)


@login_required
@require_POST
def toggle_completada(request, pk):
    """Vista para marcar/desmarcar una tarea como completada mediante AJAX"""
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    
    # Obtener datos del cuerpo de la solicitud
    try:
        data = json.loads(request.body)
        completada = data.get('completada', False)
    except json.JSONDecodeError:
        completada = not tarea.completada  # Si hay error, simplemente invertir el estado actual
    
    # Actualizar el estado de completado
    tarea.completada = completada
    tarea.save()
    
    # Devolver respuesta JSON
    return JsonResponse({
        'success': True,
        'completada': tarea.completada,
        'mensaje': f'Tarea {"completada" if tarea.completada else "marcada como pendiente"} exitosamente'
    })
