from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library

# === FUNCTION-BASED VIEW: List all books ===
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# === CLASS-BASED VIEW: Library Detail (with all books) ===
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

