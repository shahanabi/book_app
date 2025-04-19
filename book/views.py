from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        Register.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password  # Note: Storing raw password like this is not safe for real apps
        )

        return redirect('homepage')

    return render(request, 'register.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_view.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        cover = request.FILES.get('cover')  # this is the uploaded image

        Book.objects.create(
            title=title,
            author=author,
            description=description,
            price=price,
            cover=cover  # make sure your model field is named `covers`
        )
        return redirect('book_list')  # replace with your actual view name or URL name

    return render(request, 'add_book.html')


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.price = request.POST.get('price')

        if 'cover' in request.FILES:
            book.cover = request.FILES['cover']

        book.save()
        return redirect('book_list')

    return render(request, 'edit_book.html', {'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        book.delete()
        return redirect('book_list')  # Redirect to the book list after deletion

    return render(request, 'delete_book_confirm.html', {'book': book})


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    userdetails = Register.objects.filter(email=email, password=password).first()
    if userdetails: 
        request.session['rid'] = userdetails.id
        request.session['rname'] = userdetails.name
        request.session['email'] = email
        request.session['ruser'] = 'ruser'

        return render(request, 'homepage.html')  # Ensure this file exists in your templates folder

    
    return render(request, 'login.html', {'status': 'Invalid email or password'})

def logout(request):
    session_key = list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return redirect(homepage)

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})