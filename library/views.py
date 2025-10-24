from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


# 📘 Главная страница — список книг
def books_list(request):
    books_expensive = Book.objects.filter(price__gt=2000)
    books_after_2010 = Book.objects.filter(year__gt=2010).order_by('year')
    books_tolstoy = Book.objects.filter(author__icontains='толстой')

    context = {
        'books_expensive': books_expensive,
        'books_after_2010': books_after_2010,
        'books_tolstoy': books_tolstoy,
    }
    return render(request, 'library/books.html', context)


# 🔍 Поиск книг по автору
def search_books(request):
    query = request.GET.get('q', '')
    results = Book.objects.filter(author__icontains=query) if query else []
    return render(request, 'library/search.html', {'query': query, 'results': results})


# ➕ Добавление новой книги
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})


# ✏️ Редактирование книги
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_book.html', {'form': form, 'book': book})


# 🗑 Удаление книги с подтверждением
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':  # если нажал "Да, удалить"
        book.delete()
        return redirect('books_list')
    return render(request, 'library/delete_book.html', {'book': book})
