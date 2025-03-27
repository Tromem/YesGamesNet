from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.forms import ModelForm




class Buyer(AbstractUser):
    
    description = models.TextField(verbose_name='Описание продавца',name='overviev',max_length='1000' ,blank=True)
    userpic = models.ImageField(upload_to='media', blank=True,verbose_name='фото')

 
class Comment(models.Model):
    object_id = models.PositiveIntegerField('ИД поста', default=1)
    Fromuser = models.ForeignKey(Buyer , 
                                 on_delete=models.CASCADE,
                                 related_name='comment_fromUser')
    
    recepiend = models.ForeignKey(Buyer , 
                                  on_delete=models.CASCADE,
                                  related_name="comments_received",)
    
    text = models.TextField(verbose_name='комментарий', max_length=200)
    created = models.DateTimeField(default=timezone.now )
    
    def __str__(self):
        return self.text
        
       
    