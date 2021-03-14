from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

User = get_user_model()


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:
    @staticmethod
    def get_products_for_main_page(self, *args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to),
                                  reverse=True)
        return products


class LatestProducts:
    object = LatestProductsManager()


# Category


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категории')
    slug = models.SlugField(unique=True, verbose_name='Уник URL')

    def __str__(self):
        return self.name


# Product


class Product(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100, verbose_name='Продукт(Наименование)')
    slug = models.SlugField(unique=True, verbose_name='Slug(Уник URL)')
    image = models.ImageField(verbose_name='Изобажение')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Products (Sofa,Armchair,Bed,Table)

class Sofa(Product):
    materials = models.CharField(max_length=255, verbose_name='Материалы')
    back = models.CharField(max_length=100, verbose_name='Ткань')
    width = models.PositiveSmallIntegerField(max_length=255, verbose_name='Ширина')
    height = models.PositiveSmallIntegerField(max_length=255, verbose_name='Высота')
    length = models.PositiveSmallIntegerField(max_length=255, verbose_name='Длина')
    weight = models.PositiveSmallIntegerField(max_length=255, verbose_name='Масса')
    color = models.CharField(max_length=50, verbose_name='Цвет')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Bed(Product):
    materials = models.CharField(max_length=255, verbose_name='Материалы')
    width = models.PositiveSmallIntegerField(max_length=255, verbose_name='Ширина')
    height = models.PositiveSmallIntegerField(max_length=255, verbose_name='Высота')
    length = models.PositiveSmallIntegerField(max_length=255, verbose_name='Длина')
    weight = models.PositiveSmallIntegerField(max_length=255, verbose_name='Масса')
    color = models.CharField(max_length=50, verbose_name='Цвет')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Table(Product):
    materials = models.CharField(max_length=255, verbose_name='Материалы')
    width = models.PositiveSmallIntegerField(max_length=255, verbose_name='Ширина')
    height = models.PositiveSmallIntegerField(max_length=255, verbose_name='Высота')
    length = models.PositiveSmallIntegerField(max_length=255, verbose_name='Длина')
    weight = models.PositiveSmallIntegerField(max_length=255, verbose_name='Масса')
    color = models.CharField(max_length=50, verbose_name='Цвет')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


# Cartproduct


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    count = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return "Продукт {}".format(self.product.title)


# Cart


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name="Владелец", on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return str(self.id)


# Order


# Customer


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    address = models.CharField(max_length=100, verbose_name="Адрес")

    def __str__(self):
        return "Покупатель {}{}".format(self.user.first_name, self.user.last_name)
