from django.contrib import admin
from .models import Buyer
from .models import Comment

admin.site.register(Buyer)
admin.site.register(Comment)