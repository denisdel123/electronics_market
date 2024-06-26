from django.conf import settings
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='category/', **NULLABLE, verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, **NULLABLE, verbose_name='Наименование товара')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Фото')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.CharField(max_length=30, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='в наличии')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name, self.category, self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [(
            'set_published',
            'Can publish posts'
        )]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_version = models.IntegerField(verbose_name='Номер версии')
    name_version = models.CharField(max_length=150, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Признак')

    def __str__(self):
        return f'{self.product}, {self.name_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
