from django import forms

class userRegisterForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField()