from . import views
from django.urls import path,include

urlpatterns = [
    path('profile/', views.UserProfileView, name='profile'),
    path('register', views.RegisterView.as_view(),name='register' ),
    path('profiles/<int:pk>', views.UserDetails.as_view(), name='user-detail')
    

]
