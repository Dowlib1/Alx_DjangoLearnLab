from django.shortcuts import render
from django.conf import settings
# users/views.py
from django.shortcuts import render, get_object_or_404
from .models import CustomUser

def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'users/profile.html', {'user': user})
class SomeOtherModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# Create your views here.
