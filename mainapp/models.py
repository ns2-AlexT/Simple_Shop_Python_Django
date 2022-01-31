from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('name', max_length=64)
    description = models.TextField('description', blank=True)
    is_active = models.BooleanField('is_active', default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category of product'
        verbose_name_plural = 'Categories of product'
        ordering = ('id', 'name')

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save(using=using)


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=64)
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField('description', blank=True)
    price = models.DecimalField('price', max_digits=6, decimal_places=2, default=0)
    quantity = models.IntegerField('quantity', default=0)
    sale_atr = models.BooleanField('sale_attr', default=True)
    is_active = models.BooleanField('is_active', default=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
