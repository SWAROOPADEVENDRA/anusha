from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def baby(request):
    return render(request,'baby.html')


def a1(request):
    return HttpResponse('Hi Anusha')