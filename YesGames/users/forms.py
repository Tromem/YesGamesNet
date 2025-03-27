from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Buyer , Comment
from django import forms
from django.forms import ModelForm

User = get_user_model()


class RegisterForm(UserCreationForm):
        
    
    class Meta():
        model = Buyer
        fields = ('username','password1','password2','userpic')
        
        
        
class CreateComment(ModelForm):
    
    class Meta:
        model = Comment
        fields = ("text",) 