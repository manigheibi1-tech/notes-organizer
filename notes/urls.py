from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('register/', views.register, name='register'),
    path('new/', views.course_create, name='course_create'),
    path('<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('<int:course_pk>/notes/', views.note_list, name='note_list'),
    path('<int:course_pk>/notes/new/', views.note_create, name='note_create'),
    path('<int:course_pk>/notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('<int:course_pk>/notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('<int:course_pk>/notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
]