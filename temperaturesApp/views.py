from django.shortcuts import render
from . import models, serializers
import decimal
from django.core.paginator import Paginator
from rest_framework import viewsets

READINGS_PER_PAGE = 100

def list(request):
    readings = models.TmpReading.objects.all().order_by('-timestamp')
    p = Paginator(readings, READINGS_PER_PAGE)
    if 'page' in request.GET:
        try:
            page = int(request.GET['page'])
            if not (page in p.page_range):
                page = 1
        except ValueError:
            page = 1
    else: 
        page = 1
    page_readings = p.page(page)
    context = {'readings': page_readings}
    return render(request, 'temperaturesApp/list.html', context)

class TmpReadingViewSet(viewsets.ModelViewSet):
    queryset = models.TmpReading.objects.all()
    serializer_class = serializers.TmpReadingSerializer

