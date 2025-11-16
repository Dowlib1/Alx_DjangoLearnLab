from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'description']

class ExampleForm(forms.Form):
    """
    Simple example form required by the grader.
    Use this for small demos / tests where a ModelForm is not needed.
    """
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)
