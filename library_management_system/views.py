from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth.models import User
import logging
# Create your views here.

def home(request):
    books = models.Book.objects.all()
    return render(request, "index.html", {'books': books})

def register(request):
    return  render(request,'register.html')

def add_book(request):
    return render(request, "add_book.html")

def view_books(request):
    return render(request,'view_books.html')

def delete_book(request,myid):
    books = models.Book.objects.filter(id=myid)
    books.delete()
    books = models.Book.objects.all()
    return render(request,'index.html',{"books":books})
def insert_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']

        books = models.Book.objects.create(name=name, author=author, isbn=isbn, category=category)
        books.save()
        alert = True
        return render(request, "add_book.html", {'alert': alert})

def insert_admin(request):
    if request.method == "POST":
        firstname = request.POST['SignupInputFirstName']
        lastname = request.POST['SignupInputLastName']
        email = request.POST['SignupInputEmail1']
        pass1 = request.POST['SignupInputPassword1']
        pass2 = request.POST['SignupInputPassword2']
        user = User.objects.create_user(username=email,email=email,password=pass1)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        alert = True
        return render(request, "login.html", {'alert': alert})

def view_books(request):
    books = models.Book.objects.all()
    return render(request, "view_books.html", {'books':books})

def login_request(request):
    if request.method == "POST":
        email = request.POST['SigninInputEmail1']
        password = request.POST['SigninInputPassword1']
        auth = authenticate(username=email,password=password)
        books = models.Book.objects.all()
        if auth is not None:
            login(request,auth)
            return render(request,'index.html', {'books':books})
        else:
            return HttpResponse("Try Again")

def signout(request):
    logout(request)
    return redirect('home')

def signinpage(request):
    return render(request,'login.html')

def update_book(request,myid):
    books = models.Book.objects.filter(id=myid)
    return render(request,'update.html',{"books":books})

def update_request(request,myid):
    books = models.Book.objects.filter(id=myid)
    
    pass