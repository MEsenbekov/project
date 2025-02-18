from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .form import BookForm
from .models import Book


def book_list(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    books = Book.objects.all()
    return render(request, 'Books/books_list.html', {'form': form, 'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_title = form.cleaned_data['title']

            if Book.objects.filter(title=book_title).exists():
                form.add_error('title', 'Книга с таким названием уже существует.')
                return render(request, 'Books/add_book.html', {'form': form})

            try:
                form.save()
                return redirect('book_list')
            except IntegrityError:
                form.add_error('title', 'Ошибка базы данных. Попробуйте снова.')
    else:
        form = BookForm()

    return render(request, 'Books/add_book.html', {'form': form})


class BookDeleteView(DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')

# Create your views here.
