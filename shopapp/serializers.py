from rest_framework import serializers
from .models import Section, Subsection, Category, Product
from .modeldetail import SubsectionDetail, CategoryDetail, ProductDetail

# simple serializers
class SectionSerializer(serializers.ModelSerializer):
        class Meta:
                model = Section
                fields = '__all__'

class SubsectionSerializer(serializers.ModelSerializer):
        class Meta:
                model = Subsection
                fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
        class Meta:
                model = Category
                fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
        class Meta:
                model = Product
                fields = '__all__'

# detail serializers
class SubsectionDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = SubsectionDetail
                fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = CategoryDetail
                fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = ProductDetail
                fields = '__all__'
