from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course

@login_required
def course_list(request):
    courses = Course.objects.filter(owner=request.user)
    return render(request, 'notes/course_list.html', {'courses': courses})