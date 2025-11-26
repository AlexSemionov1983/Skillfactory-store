from django.forms import ModelForm, BooleanField
from .models import Product


# Создаём модельную форму
class ProductForm(ModelForm):
    check_box = BooleanField(label="Алло, Галочка!")
    # В класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'quantity', 'check_box']
