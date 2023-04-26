from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Products
# Create your models here.

class CreateUserForm(UserCreationForm):
    class Meta : 
        model = User
        fields = ['username', 'password1', 'email', 'password2' ]
        
    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()
        password = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        # if password != password2:
        #     raise forms.ValidationError('password and Confirm Password do not match !')
        

class CreateProductForm(forms.ModelForm):
    
    class Meta : 
        model = Products
        fields = ['title', 'picture', 'price', 'desc', 'count']