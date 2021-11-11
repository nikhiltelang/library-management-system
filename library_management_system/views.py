from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def register(request):
    return  render(request,'register.html')

def add_book(request):
    return render(request,'add_book.html')

def view_books(request):
    return render(request,'view_books.html')