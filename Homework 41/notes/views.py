from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Category
from .forms import NoteForm

# Notes list
def note_list(request):
    notes = Note.objects.all()

    # filtration
    category = request.GET.get('category')
    search = request.GET.get('search')
    reminder = request.GET.get('reminder')

    if category:
        notes = notes.filter(category__title__icontains=category)
    if search:
        notes = notes.filter(title__icontains=search)
    if reminder:
        notes = notes.filter(reminder__date=reminder)

    return render(request, 'notes/note_list.html', {'notes': notes})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_detail.html', {'form': form, 'note': note})


def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_edit.html', {'form': form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
