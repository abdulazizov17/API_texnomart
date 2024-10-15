from rest_framework import serializers
from texnomart.models import Category, Product, Image,Comment,AttributeKey,AttributeValue,ProductAttribute
from django.db.models import Avg


class CategorySerializer(serializers.ModelSerializer):
    full_image_url = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField(method_name='groups_count')

    def groups_count(self, obj):
        count = obj.groups.count()
        return count

    def get_full_image_url(self, instance):

        if instance.image:
            image_url = instance.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url)
        else:
            return None

    class Meta:
        model = Category
        fields = ['id', 'title', 'full_image_url', 'slug', 'count', 'groups']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['message', 'file', 'rating', 'user', 'created_at']






class ProductSerializer(serializers.ModelSerializer):
    all_images = serializers.SerializerMethodField()
    users_like = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.title', default='No Category', allow_blank=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()

    def get_avg_rating(self, instance):
        avg = instance.comments.aggregate(avg_rating=Avg('rating'))
        return round(avg['avg_rating']) if avg['avg_rating'] else 0

    def get_users_like(self, product):
        user = self.context.get('request').user
        return user.is_authenticated and user in product.users_like.all()

    def get_all_images(self, instance):
        request = self.context.get('request')
        return [request.build_absolute_uri(image.image.url) for image in instance.images.all()]

    def to_representation(self, product):
        context = super().to_representation(product)
        context['comments_count'] = product.comments.count()
        return context

    class Meta:
        model = Product
        fields = '__all__'

class AttributeKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeKey
        fields = ['id', 'key_name']

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ['id', 'key_value']

class ProductAttributeSerializer(serializers.ModelSerializer):
    attr_key = AttributeKeySerializer()
    attr_value = AttributeValueSerializer()
    product = serializers.StringRelatedField()

    class Meta:
        model = ProductAttribute
        fields = ['id', 'attr_key', 'attr_value', 'product']





