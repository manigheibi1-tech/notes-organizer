from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/courses/register/'), name='home'),
    path('admin/', admin.site.urls),
    path('courses/', include('notes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]