from django import forms

class ChekoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)