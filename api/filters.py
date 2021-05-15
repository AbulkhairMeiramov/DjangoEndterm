from django_filters import rest_framework as filters
from api.models import Category


class CategoryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Category
        fields = ('name',)
