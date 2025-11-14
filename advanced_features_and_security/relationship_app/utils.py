from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

admin_required = user_passes_test(is_admin, login_url='/relationship_app/login/')(lambda x: True)
librarian_required = user_passes_test(is_librarian, login_url='/relationship_app/login/')(lambda x: True)
member_required = user_passes_test(is_member, login_url='/relationship_app/login/')(lambda x: True)

