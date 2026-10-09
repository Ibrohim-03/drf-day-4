from rest_framework import serializers
from .models import User,Product,Category,Review
from django.db.models import Avg

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = 'category',
        write_only = True
    )
    owner = UserSerializer(read_only = True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'owner',
        write_only = True
    )
    def validate_price(self,value):
        if value<0:
            raise serializers.ValidationError(
                "Price should be positive number"
            )
        return value

    def validate_title(self,value):
        if not value:
            raise serializers.ValidationError(
                "Title shouldnt be empty"
            )
        return value

    
    class Meta:
        model = Product
        fields = ['title','description','price','category','category_id','owner','owner_id','created_at']


class ReviewSerilaizer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset = Product.objects.all(),
        source = 'product',
        write_only = True
    )
    user = UserSerializer(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user',
        write_only = True
    )
    def validate_rating(self,value):
        if value<0 and value>5:
            raise serializers.ValidationError(
                "Rating should be positive and not more than 5"
            )
        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        avg = instance.rating.aggregate(Avg('rating'))['rating__avg']
        rep["avg_rating"] = round(avg, 1) if avg is not None else 0.0
        
        return rep
    

    class Meta:
        model = Review
        fields = ['text','rating','product','product_id','user','user_id']