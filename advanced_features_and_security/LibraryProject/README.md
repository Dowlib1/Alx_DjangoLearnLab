```text
Permissions & Groups Setup for Bookshelf (quick guide)

1) Files updated/added:
   - models.py: Book model now defines custom permissions (can_view, can_create, can_edit, can_delete)
   - forms.py: BookForm ModelForm
   - views.py: permission-protected views using @permission_required('bookshelf.can_*')
   - management/commands/setup_groups.py: create groups and assign permissions

2) Commands to run (from project root):
   pip install Pillow           # only if ImageField used elsewhere
   python manage.py makemigrations bookshelf
   python manage.py makemigrations   # run for any other apps changed
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py setup_groups
   python manage.py runserver

3) Manual testing steps:
   - Log into /admin as superuser.
   - Under AUTHENTICATION AND AUTHORIZATION -> Groups, confirm:
       Viewers   -> has 'Can view book'
       Editors   -> has 'Can view book', 'Can create book', 'Can edit book'
       Admins    -> has all four can_* permissions
   - Create test users and assign them to groups.
   - Verify:
       - Viewer: can access book_list but gets 403 on create/edit/delete.
       - Editor: can create and edit but not delete.
       - Admin: can create, edit and delete.

4) Notes:
   - Permission codenames MUST be exactly: can_view, can_create, can_edit, can_delete
   - Views use permission_required('bookshelf.<codename>', raise_exception=True)
   - Use settings.AUTH_USER_MODEL for user FK compatibility with custom user model
```
