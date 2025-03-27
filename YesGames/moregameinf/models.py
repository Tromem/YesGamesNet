from django.db import models
from users.models import Buyer

class Goods():

    GoodsName = models.TextField(verbose_name="название", max_length=40)
    prise = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='описание',max_length=1000)
    images = models.ImageField('фото товара',upload_to='media/goods')
    byUser = models.ForeignKey(Buyer , on_delete=models.CASCADE)


