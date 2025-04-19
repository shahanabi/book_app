from django.urls import path, include
from . import views


urlpatterns =[
    path('', views.homepage, name='homepage'),

    path('register/', views.register, name='register'),

    path('book_list/', views.book_list, name='book_list'),

    path('add_book/', views.add_book, name='add_book'),

    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),

    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    path('login/', views.login, name='login'),

    path('logout/', views.logout, name='logout'),

    path('books/', views.books, name='books'),


]