from django import forms
from django.template.defaultfilters import length

from customers.models import Customer


# this is a django form
# a django form only creates half a form(you cannot submit successfully as it is not complete) a model form completes this
class CustomerForm(forms.Form):
    name = forms.CharField(required=True, max_length=20, label='NAME:')
    email=forms.EmailField(required=True, min_length=10,max_length=30, label='EMAIL:')
    phone=forms.IntegerField(required=True, label='PHONE NUMBER:')
    address = forms.CharField(required=True, label='ADDRESS:')


class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        # we have to clarify which form in models is to be used
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Gender'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Age'}),
        }