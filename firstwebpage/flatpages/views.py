from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'static_handler.html')
def hello(request):
    return HttpResponse( "Привет, Мир!", content_type="text/plain;charset=UTF-8")
# Create your views here.
