from django.shortcuts import render
from production.models import Gallery

# Create your views here.


def production(request):
    title = 'Производство'
    gallery = Gallery.objects.all
    return render(request, 'production.html',
                  {'gallery': gallery, 'title': title})
