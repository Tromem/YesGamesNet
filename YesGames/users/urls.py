from . import views
from django.urls import path,include

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('register', views.RegisterView.as_view(),name='register' )
    

]
