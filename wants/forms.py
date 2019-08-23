from django import forms
from .models import Genre

class SearchForm(forms.Form):
	genre = forms.ModelChoiceField(
		queryset=Genre.objects, label='ジャンル', required=False)