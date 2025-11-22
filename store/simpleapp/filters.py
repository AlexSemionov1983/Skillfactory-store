import django_filters
from .models import Product, Category


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Название содержит',   # ← ПЕРЕИМЕНОВАНИЕ
    )

    price__gt = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gt',
        label='Цена от',             # ← ПЕРЕИМЕНОВАНИЕ
    )

    price__lt = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lt',
        label='Цена до',             # ← ПЕРЕИМЕНОВАНИЕ
    )

    quantity = django_filters.NumberFilter(
        field_name='quantity',
        lookup_expr='gt',
        label='Количество больше',   # ← ПЕРЕИМЕНОВАНИЕ
    )

    # Категорию возвращаем КАК БЫЛО: normal ModelChoiceFilter
    category = django_filters.ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория'
    )

    class Meta:
        model = Product
        fields = ()
