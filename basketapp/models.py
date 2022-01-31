from django.contrib.auth import get_user_model
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_p = models.PositiveIntegerField('quantity', default=0)
    datetime_add = models.DateTimeField('date of add', auto_now_add=True)
    datatime_upd = models.DateTimeField('date of update', auto_now=True)

    @property
    def product_total_cost_(self):
        return self.product.price * self.quantity_p
