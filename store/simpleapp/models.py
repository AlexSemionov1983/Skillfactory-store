from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


# Товар для нашей витрины
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f'{self.name}: {self.quantity}'

    def get_absolute_url(self):
        return f'/products/{self.id}'

# Категория, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
