from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.s


def index(request):
    return HttpResponse("aaaa")

# def index(request):
#     return render(request, "index.html")