from django.urls import path
# Импортируем созданное нами представление
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', Products.as_view()),
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),  # Ссылка на создание товара
    path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

]
