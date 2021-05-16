import logging
from django.shortcuts import render
from api.models import Category, Product, Comment
from auth_.models import MainUser
from api.serializers import CategorySerializer, ProductSerializer, CommentSerializer, ProductFullSerializer
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import CategoryFilter
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from api.permissions import USER_ROLE_SUPER_USER, USER_ROLE_CLIENT
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

logger = logging.getLogger(__name__)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)

    filterset_class = CategoryFilter
    search_fields = ('name',)
    ordering_fields = ('name',)

    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Category.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Category object created, ID: {serializer.instance}')
        logger.info(f'Category object created, ID: {serializer.instance}')
        logger.warning(f'Category object created, ID: {serializer.instance}')
        logger.error(f'Category object created, ID: {serializer.instance}')
        logger.critical(f'Category object created, ID: {serializer.instance}')

    # def list(self, request, pk):
    #     serializer = CategorySerializer(self.get_queryset(), many=True)
    #     return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='inactive', url_name='in_active', permission_classes=(AllowAny,))
    def not_active(self, request):
        logger.debug('not_active')
        queryset = Category.objects.filter(is_active=False)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False, permission_classes=(IsAuthenticated,))
    def create_category(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response('OK')


class ProductListAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    logger.debug('Product created')
    queryset = Product.objects.all()
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CommentViewSet(viewsets.ModelViewSet):
    logger.debug('Comment created')
    queryset = Comment.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET', 'POST'])
def product_comment(self, request, pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(product_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('OK')


@api_view(['GET', 'POST'])
def category_product(request, pk):
    if request.method == 'GET':
        product = Product.objects.filter(category_id=pk)
        serializer = ProductFullSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductFullSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('OK')


