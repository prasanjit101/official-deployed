from django import forms

class UserContact(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    number = forms.IntegerField()
    message = forms.CharField()