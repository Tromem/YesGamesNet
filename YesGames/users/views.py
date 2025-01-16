from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import logout 
from django.views import View


class RegisterView(View):

    template_name = 'registration/registration.html'
    success_url = reverse_lazy('profile')

    def get(self,req):
        context = {
            'form': RegisterForm()

        }
        return render(req,self.template_name,context)
    def post(self,req):
        if req.method == 'POST':
            form = RegisterForm(req.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data('username')
                password = form.cleaned_data('username')
                user =  authenticate(username=username,password=password)
                
                login(req,user=user)
                return redirect('profile/')
            context = {
                'form': form
            }
            return render(req,self.template_name,context=context)

            
    
    
def logout_view(req):
    logout(req)
    pass
    

@login_required
def profile_view(req):
    return render(req, 'registration/userprofile.html')
