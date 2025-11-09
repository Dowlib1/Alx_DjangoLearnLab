from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

# === FUNCTION-BASED VIEW: Use template (optional but implemented) ===
def list_books(request):
    books = Book.objects.all()
    try:
        return render(request, 'relationship_app/list_books.html', {'books': books})
    except:
        output = "<h1>Books Available:</h1><ul>"
        for book in books:
            output += f"<li>{book.title} by {book.author.name}</li>"
        output += "</ul>"
        return HttpResponse(output)

# === CLASS-BASED VIEW: Use template ===
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def render_to_response(self, context, **response_kwargs):
        try:
            return super().render_to_response(context, **response_kwargs)
        except:
            library = context['object']
            output = f"<h1>Library: {library.name}</h1><h2>Books in Library:</h2><ul>"
            for book in library.books.all():
                output += f"<li>{book.title} by {book.author.name}</li>"
            output += "</ul>"
            return HttpResponse(output)

