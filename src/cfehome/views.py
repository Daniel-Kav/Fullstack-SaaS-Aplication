from django.shortcuts import HttpResponse,render
from visits.models import PageVisit

def home(request):
    queryset = PageVisit.objects.all()
    PageVisit.objects.create(path = request.path)
    return render(request, 'home.html',{'queryset': queryset.count()})