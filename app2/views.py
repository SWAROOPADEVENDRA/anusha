from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def anu(request):
    return render(request,'anu.html')

def p2(request):
    return HttpResponse('Hi Pavan')