from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', views.readarduino),
    path('funky', views.funky),
    path('admin/', admin.site.urls),
    path('danger', views.danger),
    path('rest/<int:guess>', views.rest)
]
