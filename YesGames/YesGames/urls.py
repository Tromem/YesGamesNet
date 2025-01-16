
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from main import urls as main
from users import urls as users
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main)),
    path('accounts/', include("django.contrib.auth.urls")),
    path("users/", include(users))
]
