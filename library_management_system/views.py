from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth.models import User
from django.contrib import messages
from . templatestag.logger import App_Logger

# Create your views here.
log = App_Logger()
# First page of Library Management System
def home(request):
    log.info("Jump to the home page")
    books = models.Book.objects.all()
    return render(request, "index.html", {'books': books})

# Here New Registration wiil be done
def register(request):
    log.info("Jump to the Registration Page")
    return  render(request,'register.html')

# Authorized person can be Add book
def add_book(request):
    log.info("Jump to the add bok page")
    return render(request, "add_book.html")

def view_books(request):
    return render(request,'view_books.html')

# When we pressed Delete button Book will be deleted
def delete_book(request,myid):
    books = models.Book.objects.filter(id=myid)
    books.delete()
    books = models.Book.objects.all()
    log.info("Delete book Successfully",id)
    messages.success(request,"Book Delete Successfully")
    return render(request,'index.html',{"books":books})

# Here for adding New book
def insert_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']

        books = models.Book.objects.create(name=name, author=author, isbn=isbn, category=category)
        books.save()
        log.info("Add boot Successfully",name)
        messages.success(request, 'Book is Successfully Added')
        return render(request, "add_book.html")

# Here New regitsraion value stored in database
def insert_admin(request):
    if request.method == "POST":
        firstname = request.POST['SignupInputFirstName']
        lastname = request.POST['SignupInputLastName']
        email = request.POST['SignupInputEmail1']
        pass1 = request.POST['SignupInputPassword1']
        pass2 = request.POST['SignupInputPassword2']
        # if password is note same entered by user
        if pass1!=pass2:
            log.error("Password is not same",email)
            messages.error(request,"Password Must be same")
            return render(request, "register.html")
        else:
            # Password is same entered by user
            user = User.objects.create_user(username=email,email=email,password=pass1)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            log.info("User Create Successfully",email)
            messages.success(request, 'Registration Done Successfully')
            return render(request, "login.html")

# Here You will get all Books record
def view_books(request):
    books = models.Book.objects.all()
    return render(request, "view_books.html", {'books':books})

# Here check the user authorized or not
def login_request(request):
    if request.method == "POST":
        email = request.POST['SigninInputEmail1']
        password = request.POST['SigninInputPassword1']
        auth = authenticate(username=email,password=password)
        books = models.Book.objects.all()
        if auth is not None:
            login(request,auth)
            log.info("Login Sucessfully",email)
            return render(request,'index.html', {'books':books})
        else:
            log.error("Something went wrong",email)
            messages.error(request, 'Something went wrong')
            return render(request, "login.html")

# for Logout User
def signout(request):
    logout(request)
    log.info("Logout Successfully")
    return redirect('home')

# Here jump to the Login page
def signinpage(request):
    log.info("jump to the Sign in Page")
    return render(request,'login.html')

# Here Update of book will happen
def update_book(request,myid):
    log.info("Jump to the Update Book Page")
    books = models.Book.objects.filter(id=myid)
    return render(request,'update.html',{"books":books})

# Here Updation of book will happen
def update_request(request,myid):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']
        books = models.Book.objects.get(id=myid)
        books.name = name
        books.author = author
        books.isbn = isbn
        books.category = category
        books.save()
        books = models.Book.objects.all()
        log.info("Update Book Successfully",name)
        messages.success(request,"Update book Successfully")
        return render(request, "index.html", {'books': books})

# User Can change Password
def changepassword(request,id):
    if request.method == "POST":
        pass1 = request.POST['inputpassword1']
        pass2 = request.POST['inputpassword2']
        if pass1==pass2:
            users = User.objects.filter(id=id)
            user = users[0]
            user.set_password(pass1)
            user.save()
            log.info("Password Change Successfully",user)
            messages.success(request,'Password Change Successfully, You Must Have Login Once Again')
            books = models.Book.objects.all()
            return render(request, "index.html", {'books': books})
        else:
            log.error("Password is not same")
            messages.error(request, 'Password Must be same')
            books = models.Book.objects.all()
            return render(request, "index.html", {'books': books})