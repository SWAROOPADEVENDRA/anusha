from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pavan(request):
    return render(request,'pavan.html')

def nanna(request):
    return HttpResponse('My real hero')