
---

### Step 6: Create `CRUD_operations.md` (Summary)

```bash
nano CRUD_operations.md


####
# CRUD Operations Summary

All operations performed using Django ORM in `python manage.py shell`.

---

## 1. Create
- Created book: **1984** by George Orwell (1949)
- See: [create.md](./create.md)

## 2. Retrieve
- Retrieved full book details
- See: [retrieve.md](./retrieve.md)

## 3. Update
- Changed title to **Nineteen Eighty-Four**
- See: [update.md](./update.md)

## 4. Delete
- Deleted the book
- Confirmed via empty queryset
- See: [delete.md](./delete.md)

---

**Model Definition (`bookshelf/models.py`):**
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
