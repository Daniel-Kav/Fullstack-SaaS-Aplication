from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>saas application home page</h1>")