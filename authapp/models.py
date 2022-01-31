from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    ava = models.ImageField(upload_to='avatars', blank=True)
    age = models.PositiveIntegerField('age', null=True)

    def basket_p(self):
        return sum(el_pp.product.price * el_pp.quantity_p for el_pp in self.basket.all())

    def basket_c(self):
        return sum(el_pc.quantity_p for el_pc in self.basket.all())
