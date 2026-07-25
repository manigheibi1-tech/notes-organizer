from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Note
from django.contrib.auth.forms import UserCreationForm
from .forms import CourseForm, NoteForm
from django.shortcuts import get_object_or_404
from django.db.models import Q

@login_required
def course_list(request):
    courses = Course.objects.filter(owner=request.user)
    return render(request, 'notes/course_list.html', {'courses': courses})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'notes/register.html', {'form': form})

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'notes/course_form.html', {'form': form})

@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'notes/course_form.html', {'form': form})

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk, owner=request.user)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'notes/course_confirm_delete.html', {'course': course})

@login_required
def note_list(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk, owner=request.user)
    query = request.GET.get('q', '')
    notes = course.notes.all()
    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'notes/note_list.html', {'course': course, 'notes': notes, 'query': query})

@login_required
def note_create(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk, owner=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.course = course
            note.save()
            return redirect('note_list', course_pk=course.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'course': course})

@login_required
def note_edit(request, course_pk, pk):
    course = get_object_or_404(Course, pk=course_pk, owner=request.user)
    note = get_object_or_404(Note, pk=pk, course=course)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list', course_pk=course.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'course': course})

@login_required
def note_delete(request, course_pk, pk):
    course = get_object_or_404(Course, pk=course_pk, owner=request.user)
    note = get_object_or_404(Note, pk=pk, course=course)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list', course_pk=course.pk)
    return render(request, 'notes/note_confirm_delete.html', {'note': note, 'course': course})