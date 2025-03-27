from django.shortcuts import render , redirect 
from django.contrib.auth import authenticate , login
from .forms import RegisterForm ,CreateComment 
from django.urls import reverse_lazy
from django.contrib.auth import logout 
from django.views import View
from .models import Buyer 
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin




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
            form = RegisterForm(req.POST,req.FILES)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                img = form.cleaned_data['userpic']
            
                form.save()
                user =  authenticate(username=username,password=password)
                
                login(req,user=user)
                return redirect('main')
            context = {
                'form': form
            }
            return render(req,self.template_name,context=context)

            
    
    
def logout_view(req):
    logout(req)
    pass
    
class UserDetails(DetailView):
    model = Buyer
    template_name = 'moreuserinf/userview.html'
    context_object_name = 'Buyer'
   
    def get(self,req,*args, **kwargs):
        
        buyer= self.get_object()
        
        buyerComments = buyer.comments_received.all()
        UserData = {
            'Buyer':buyer,
            "Comment":buyerComments
        }

        return render(req,self.template_name,UserData)
        

    
    def post(self,req,*args, **kwargs):
        
        self.object = self.get_object()
        form = CreateComment(req.POST)
        
        
        if req.method == "POST":
            
            if form.is_valid():
                
                comment = form.save(commit=False)
                comment.Fromuser = req.user 
                comment.recepiend = self.object
                comment.save()
                
        else:
            form = CreateComment()
                       
        return redirect('user-detail',pk=self.object.pk)
                


## Логин работает ,починить ошибку со входом 
@login_required
class UserProfileView(View, LoginRequiredMixin):
    
    temlpate_name = 'registration/userprofile.html'

    def get(self ,req):
            
            return render(req,self.temlpate_name)
    
