from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length= 50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length= 30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length= 30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #gender = forms.ChoiceField(('Male', 'male'), ('Female', 'female'), default = 'male')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
