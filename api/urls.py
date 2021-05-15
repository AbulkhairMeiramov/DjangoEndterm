from django.urls import path
from api.views import CategoryViewSet, ProductListAPIView, ProductDetailAPIView, CommentViewSet, product_comment, \
    category_product
from rest_framework import routers

router = routers.SimpleRouter()
router.register('categories', CategoryViewSet, basename='api')
router.register('comments', CommentViewSet, basename='api')
# router.register('products', ProductAPIView, basename='api')

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('products/<int:pk>/comments/', product_comment),
    path('categories/<int:pk>/products/', category_product),
]

urlpatterns += router.urls
