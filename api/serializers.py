from rest_framework import serializers
from api.models import Category, Product, Comment
from auth_.models import MainUser


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    is_active = serializers.BooleanField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'is_active',)

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'),
                                           is_active=validated_data.get('is_active'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    def validate_name(self, value):
        if '_' in value:
            raise serializers.ValidationError('invalid chars in title')
        return value


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField()
    type = serializers.CharField()
    color = serializers.CharField()

    class Meta:
        model = Product
        fields = ('id', 'type', 'color', 'name', 'description', 'price', 'image', 'category_id', 'category', 'cart',)

    def validate_price(self, value):
        if value < 1:
            raise serializers.ValidationError('price must be positive')
        return value

    def validate_description(self, value):
        if '_' in value:
            raise serializers.ValidationError('invalid chars in description')
        return value


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = '__all__'


class ProductFullSerializer(ProductSerializer):
    category = CategorySerializer()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ('category',)

    def validate_price(self, value):
        if value < 1:
            raise serializers.ValidationError('price must be positive')
        return value


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    product_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    message = serializers.CharField()

    def create(self, validated_data):
        comment = Comment.objects.create(user_id=validated_data.get('user_id'),
                                         message=validated_data.get('message'),
                                         product_id=validated_data.get('product_id'))
        return comment

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.message = validated_data.get('message', instance.message)
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.save()
        return instance
