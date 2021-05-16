from django.db import models
from rest_framework import serializers
from django.conf import settings
from utils.validators import validate_extension, validate_size


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductManager(models.Manager):

    def get_by_category_with_relation(self, category_id):
        return self.get_related().filter(category_id=category_id)

    def get_by_category_without_relation(self, category_id):
        return self.filter(category_id=category_id)

    def get_related(self):
        return self.select_related('category')


# class ProductQuerySet(models.QuerySet):
#     def get_by_category(self, category_id):
#         return self.filter(category_id=category_id)
#
#     def get_related(self):
#         return self.select_related('category')


class TypeOfDevice(models.Model):
    type = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Type of Device'
        verbose_name_plural = 'Types of Device'
        abstract = True


def num_pages_range_validation(value):
    if not (1 <= value <= 10000000):
        raise serializers.ValidationError('Invalid price value')


class Product(TypeOfDevice):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.IntegerField(validators=[num_pages_range_validation])
    image = models.ImageField(upload_to='product_photos',
                              validators=[validate_size, validate_extension],
                              null=True, blank=True)

    objects = ProductManager()
    # objects = ProductQuerySet.as_manager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name


class CommentManager(models.Manager):

    def get_by_product_with_relation(self, product_id):
        return self.get_related().filter(product_id=product_id)

    def get_by_category_without_relation(self, product_id):
        return self.filter(product_id=product_id)

    def get_related(self):
        return self.select_related('product')


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    message = models.TextField(verbose_name='Message')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


