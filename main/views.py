from django.shortcuts import render, HttpResponse
from main.views import homepage, test


def homepage(request):
    return HttpResponse("hello world")

def test(request):
    return render(request, "test.html")

# Create your views here.
