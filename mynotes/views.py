from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Note
from django.http import HttpResponseRedirect

# Vista de lista de notas utilizando class-based view y LoginRequiredMixin
class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    template_name = 'mynotes/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-creation_date')

# Vista de detalle de nota utilizando class-based view y LoginRequiredMixin
class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    template_name = 'mynotes/note_detail.html'

# Vista para crear una nota
@login_required
def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(user=request.user, title=title, content=content)
            return redirect('mynotes:note_list')
    return render(request, 'mynotes/note_edit.html', {'note': None})

# Vista para actualizar una nota utilizando métodos más manuales
@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.title = request.POST.get('title', note.title)
        note.content = request.POST.get('content', note.content)
        note.save()
        return HttpResponseRedirect(reverse('mynotes:note_detail', args=[note.pk]))
    return render(request, 'mynotes/note_edit.html', {'note': note})

# Vista para eliminar una nota
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('mynotes:note_list')