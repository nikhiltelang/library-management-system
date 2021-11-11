from django.conf.urls import url, include
from django.urls import path
from  . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    path('register',views.register,name='register'),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path("insert_book/", views.insert_book, name="insert_book"),
    path("insert_admin/", views.insert_admin, name="insert_admin"),
]