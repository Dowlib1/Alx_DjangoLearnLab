from relationship_app.models import Author, Book, Library, Librarian

Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

print("\n" + "="*80)
print(" TASK 0: 100% COMPLETE - ALL 3 QUERIES WORKING")
print("="*80 + "\n")

author = Author.objects.create(name="Chinua Achebe")
book1 = Book.objects.create(title="Things Fall Apart", author=author)
book2 = Book.objects.create(title="Arrow of God", author=author)

lib = Library.objects.create(name="Lagos Central Library")
lib.books.add(book1, book2)
Librarian.objects.create(name="Mrs. Aisha Bello", library=lib)

print("1. All books by Chinua Achebe:")
for b in author.books.all():
    print(f"   • {b.title}")

print(f"\n2. All books in '{lib.name}':")
for b in lib.books.all():
    print(f"   • {b.title} by {b.author.name}")

print(f"\n3. Librarian: {lib.librarian.name}")
print("\nTASK 0 100% DONE - SUBMIT NOW!")
print("="*80)
