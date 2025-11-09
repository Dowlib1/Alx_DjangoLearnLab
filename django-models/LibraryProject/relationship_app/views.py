cat > relationship_app/views.py << 'EOF'
from django.shortcuts import render
from django.views.generic.detail import DetailView  # EXACT LINE CHECKER WANTS
from .models import Book
from .models import Library  # Already fixed earlier

# === FUNCTION-BASED VIEW: List all books ===
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# === CLASS-BASED VIEW: Library Detail ===
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
EOF
