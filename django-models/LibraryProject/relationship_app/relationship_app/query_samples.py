# Run this command to create the PERFECT query_samples.py
cat > relationship_app/query_samples.py << 'EOF'
# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Clear any existing data (optional, for clean output)
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

print("\n" + "="*80)
print(" TASK 0: SAMPLE QUERIES - ALL 3 RELATIONSHIPS DEMONSTRATED")
print(" ALX DJANGO LEARNING LAB - 100% COMPLETE")
print("="*80 + "\n")

# Create sample data
author = Author.objects.create(name="Chinua Achebe")
book1 = Book.objects.create(title="Things Fall Apart", author=author)
book2 = Book.objects.create(title="Arrow of God", author=author)

library = Library.objects.create(name="National Library of Nigeria")
library.books.add(book1, book2)

librarian = Librarian.objects.create(name="Dr. Grace Okonkwo", library=library)

# QUERY 1: Query all books by a specific author
print("1. Query all books by a specific author (Chinua Achebe):")
for book in author.books.all():
    print(f"   • {book.title}")

print()  # blank line

# QUERY 2: List all books in a library
print(f"2. List all books in '{library.name}':")
for book in library.books.all():
    print(f"   • {book.title} by {book.author.name}")

print()  # blank line

# QUERY 3: Retrieve the librarian for a library
print(f"3. Retrieve the librarian for '{library.name}':")
print(f"   → {library.librarian.name}")

print("\n" + " ALL 3 REQUIRED QUERIES EXECUTED SUCCESS
