from django.db import models

from eco_market.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='category_photos/')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    photo = models.ImageField(upload_to='product_photos/')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    reference_point = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    total_order_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, default=0)

    # def save(self, *args, **kwargs):
    #     total_order_price = 0
    #     for product in self.products.all():
    #         total_order_price += product.total_price
    #     self.total_order_price = total_order_price
    #     super().save(*args, *kwargs)

    class Meta:
        ordering = ['-created']


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
