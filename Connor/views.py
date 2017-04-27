from django.shortcuts import render

# Create your views here.


def index(request):
    #request.POST
    #request.GET
    return render(request, "index.html")