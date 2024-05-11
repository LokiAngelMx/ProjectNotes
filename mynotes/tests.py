import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note

def create_note(user, title, content, days=0):
    """
    Crea una nota con el título y contenido dado, y una fecha de creación
    offset por el número de días especificado.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Note.objects.create(user=user, title=title, content=content, creation_date=time)

# Verifica las operaciones básicas del modelo Note como la creación, actualización y eliminación.
class NoteModelTests(TestCase):
    def test_note_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        note = create_note(user=user, title="Test Note", content="Just a test", days=-1)
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.content, "Just a test")
        self.assertTrue((timezone.now() - note.creation_date).days < 1)

    def test_note_update(self):
        user = User.objects.create_user(username='testuser', password='12345')
        note = create_note(user=user, title="Old Title", content="Just a test", days=-1)
        note.title = "New Title"
        note.save()
        updated_note = Note.objects.get(id=note.id)
        self.assertEqual(updated_note.title, "New Title")

    def test_note_deletion(self):
        user = User.objects.create_user(username='testuser', password='12345')
        note = create_note(user=user, title="Test Note", content="Just a test", days=-1)
        note_id = note.id
        note.delete()
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(pk=note_id)

# Verifica las operaciones básicas de las vistas de la aplicación mynotes.
class NoteListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_no_notes(self):
        response = self.client.get(reverse("mynotes:note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['notes'], [])

    def test_note_list(self):
        create_note(user=self.user, title="Test Note 1", content="Just a test", days=-1)
        create_note(user=self.user, title="Test Note 2", content="Another test", days=-1)
        response = self.client.get(reverse("mynotes:note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notes']), 2)

# Verifica las operaciones básicas de la vista de detalle de una nota.
class NoteDetailViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_note_detail_view(self):
        note = create_note(user=self.user, title="Test Note", content="Just a test", days=-1)
        url = reverse("mynotes:note_detail", args=(note.id,))
        response = self.client.get(url)
        self.assertContains(response, note.title)
        self.assertContains(response, note.content)