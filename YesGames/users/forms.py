from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Buyer

User = get_user_model()


class RegisterForm(UserCreationForm):
        

    class Meta():
        model = Buyer
        fields = ('username','password1','password2')
        
        
        
