from django.urls import path
from . import views

app_name = "mynotes"
urlpatterns = [
    # Ruta para la lista de todas las notas
    path("", views.NoteListView.as_view(), name="note_list"),
    # Ruta para ver los detalles de una nota específica
    path("<int:pk>/", views.NoteDetailView.as_view(), name="note_detail"),
    # Ruta para crear una nueva nota
    path("new/", views.note_create, name="note_create"),
    # Ruta para editar una nota existente
    path("<int:pk>/edit/", views.note_update, name="note_update"),
    # Ruta para eliminar una nota
    path("<int:pk>/delete/", views.note_delete, name="note_delete"),
]