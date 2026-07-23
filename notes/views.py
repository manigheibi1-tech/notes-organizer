from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from django.contrib.auth.forms import UserCreationForm

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