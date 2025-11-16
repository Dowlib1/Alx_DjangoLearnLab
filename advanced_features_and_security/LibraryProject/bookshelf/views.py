from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.http import require_http_methods
from .models import Book
from .forms import BookForm

# Simple helper to add a CSP header to a response (optional if you use django-csp)
def add_csp_header(response):
    # Keep this very strict; modify to fit your external resources
    csp = "default-src 'self'; script-src 'self' cdnjs.cloudflare.com; style-src 'self' cdnjs.cloudflare.com; img-src 'self' data:;"
    response['Content-Security-Policy'] = csp
    return response


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    q = request.GET.get('q')
    if q:
        books = Book.objects.filter(title__icontains=q)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect('bookshelf:book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
 #  return add_csp_header(resp)

@permission_required('bookshelf.can_edit', raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/form_example.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
@require_http_methods(["POST"])
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('bookshelf:book_list')from django.shortcuts import render

# Create your views here.
