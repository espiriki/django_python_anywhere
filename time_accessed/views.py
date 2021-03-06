from django.http import HttpResponse
from .models import TimeAcessed
from django.views import generic

class AccessView(generic.ListView):
    template_name = 'time_accessed/index.html'
    context_object_name = 'time_list'

    def get_queryset(self):
        """Return the last five published questions."""

        list_ = TimeAcessed.objects.all()

        list_ = list_[::-1]

        list_ = list_[:30]

        return list_