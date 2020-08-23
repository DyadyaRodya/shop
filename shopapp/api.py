from .models import Section, Subsection, Category, Product
from rest_framework import viewsets, permissions
from .serializers import SectionSerializer, SubsectionSerializer, CategorySerializer, ProductSerializer

class SectionViewSet(viewsets.ModelViewSet):
        queryset = Section.objects.all()
        permission_classes = [
                permissions.AllowAny
        ]
        serializer_class = SectionSerializer

class SubsectionViewSet(viewsets.ModelViewSet):
        queryset = Subsection.objects.all()
        permission_classes = [
                permissions.AllowAny
        ]
        serializer_class = SubsectionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        permission_classes = [
                permissions.AllowAny
        ]
        serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        permission_classes = [
                permissions.AllowAny
        ]
        serializer_class = ProductSerializer