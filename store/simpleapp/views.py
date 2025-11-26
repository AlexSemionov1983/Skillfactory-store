# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category
from datetime import datetime
from .filters import ProductFilter
from .forms import ProductForm


class Products(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'product_list.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 4  # ← количество товаров на странице


    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.now()
        context['next_sale'] = 'Распродажа в среду!'
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context


# дженерик для получения деталей о товаре
class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'