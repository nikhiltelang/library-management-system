from django.conf.urls import url, include
from django.urls import path
from  . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    path('register',views.register,name='register'),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),
]