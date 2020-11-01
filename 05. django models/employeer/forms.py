from django import forms

class EmployeerForm(forms.Form):
    username = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=20)
    password = forms.CharField(max_length=20)
