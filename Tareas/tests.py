from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tarea
from django.utils import timezone
import json
from django.core.exceptions import ValidationError

# Create your tests here.

class TareaModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.tarea = Tarea.objects.create(
            titulo='Test Tarea',
            descripcion='Test Descripción',
            usuario=self.user
        )

    def test_tarea_creation(self):
        """Test that a tarea can be created"""
        self.assertEqual(self.tarea.titulo, 'Test Tarea')
        self.assertEqual(self.tarea.descripcion, 'Test Descripción')
        self.assertEqual(self.tarea.usuario, self.user)
        self.assertFalse(self.tarea.completada)
        self.assertEqual(self.tarea.prioridad, 'media')

    def test_tarea_str_representation(self):
        """Test the string representation of a tarea"""
        self.assertEqual(str(self.tarea), 'Test Tarea')

    def test_tarea_prioridad_choices(self):
        """Test that only valid priority choices are accepted"""
        tarea = Tarea(
            titulo='Invalid Priority',
            descripcion='Test',
            usuario=self.user,
            prioridad='invalid'
        )
        with self.assertRaises(ValidationError):
            tarea.full_clean()

class TareaViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.tarea = Tarea.objects.create(
            titulo='Test Tarea',
            descripcion='Test Descripción',
            usuario=self.user
        )
        self.login_url = reverse('login')
        self.tarea_list_url = reverse('tarea_list')
        self.tarea_create_url = reverse('tarea_create')
        self.tarea_update_url = reverse('tarea_update', args=[self.tarea.pk])
        self.tarea_delete_url = reverse('tarea_delete', args=[self.tarea.pk])
        self.toggle_completada_url = reverse('toggle_completada', args=[self.tarea.pk])

    def test_tarea_list_view_requires_login(self):
        """Test that tarea list view requires login"""
        response = self.client.get(self.tarea_list_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{self.login_url}?next={self.tarea_list_url}')

    def test_tarea_list_view_with_login(self):
        """Test tarea list view with authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.tarea_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Tarea')

    def test_tarea_create_view(self):
        """Test tarea creation"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.tarea_create_url, {
            'titulo': 'Nueva Tarea',
            'descripcion': 'Nueva Descripción',
            'prioridad': 'alta'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tarea.objects.filter(titulo='Nueva Tarea').exists())

    def test_tarea_create_view_invalid_data(self):
        """Test tarea creation with invalid data"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.tarea_create_url, {
            'titulo': '',  # Invalid: empty title
            'descripcion': 'Nueva Descripción',
            'prioridad': 'alta'
        })
        self.assertEqual(response.status_code, 200)  # Should return form with errors
        self.assertFalse(Tarea.objects.filter(descripcion='Nueva Descripción').exists())

    def test_tarea_update_view(self):
        """Test tarea update"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.tarea_update_url, {
            'titulo': 'Tarea Actualizada',
            'descripcion': 'Descripción Actualizada',
            'prioridad': 'baja'
        })
        self.assertEqual(response.status_code, 302)
        self.tarea.refresh_from_db()
        self.assertEqual(self.tarea.titulo, 'Tarea Actualizada')

    def test_tarea_delete_view(self):
        """Test tarea deletion"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.tarea_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tarea.objects.filter(pk=self.tarea.pk).exists())

    def test_toggle_completada_view(self):
        """Test toggling tarea completion status"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            self.toggle_completada_url,
            json.dumps({'completada': True}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.tarea.refresh_from_db()
        self.assertTrue(self.tarea.completada)

    def test_toggle_completada_view_invalid_json(self):
        """Test toggling tarea completion status with invalid JSON"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            self.toggle_completada_url,
            'invalid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.tarea.refresh_from_db()
        self.assertFalse(self.tarea.completada)
