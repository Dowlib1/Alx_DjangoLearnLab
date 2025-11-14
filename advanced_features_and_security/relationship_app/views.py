cat > relationship_app/views.py << 'EOF'
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required  # EXACT STRING
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from .forms import BookForm

# === TASK 2: AUTH ===
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# === TASK 1: LIST VIEWS ===
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# === TASK 3: ROLE VIEWS ===
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin' if hasattr(user, 'userprofile') else False
def is_librarian(user):
    return user.userprofile.role == 'Librarian' if hasattr(user, 'userprofile') else False
def is_member(user):
    return user.userprofile.role == 'Member' if hasattr(user, 'userprofile') else False

@user_passes_test(is_admin)
def admin_view(request): return render(request, 'relationship_app/admin_view.html')
@user_passes_test(is_librarian)
def librarian_view(request): return render(request, 'relationship_app/librarian_view.html')
@user_passes_test(is_member)
def member_view(request): return render(request, 'relationship_app/member_view.html')

# === TASK 4: BOOK CRUD WITH @permission_required ===
@permission_required('relationship_app.can_add_book', raise_exception=True)  # EXACT
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added!')
            return redirect('relationship_app:book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)  # EXACT
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated!')
            return redirect('relationship_app:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)  # EXACT
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted!')
        return redirect('relationship_app:book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})
EOF
