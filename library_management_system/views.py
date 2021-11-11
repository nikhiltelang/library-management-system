from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import models
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
    return redirect("/view_books")
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

        admin = models.User.objects.create(firstname=firstname,lastname=lastname, email=email, password=pass1)
        admin.save()
        alert = True
        return render(request, "login.html", {'alert': alert})

def view_books(request):
    books = models.Book.objects.all()
    return render(request, "view_books.html", {'books':books})

def auth(request):
    if request.method == "POST":
        email = request.POST['SigninInputEmail1']
        password = request.POST['SigninInputPassword1']

        auth = authenticate(email,password)

