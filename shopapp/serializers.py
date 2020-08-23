from rest_framework import serializers
from .models import Section, Subsection, Category, Product

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
