from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculat():
    x=1
    y=2
    return x

def say_hello(request):
    x = calculat()
    return render(request, 'hello.html')
