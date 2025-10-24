from django.shortcuts import render
from .models import Book

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

def search_books(request):
    query = request.GET.get('q', '')
    results = Book.objects.filter(author__icontains=query) if query else []
    return render(request, 'library/search.html', {'query': query, 'results': results})
