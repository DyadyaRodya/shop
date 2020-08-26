from .models import Section, Subsection, Category, Product
from rest_framework import viewsets, permissions
from .serializers import SectionSerializer, SubsectionSerializer, CategorySerializer, ProductSerializer
from .serializers import SubsectionDetailSerializer, CategoryDetailSerializer, ProductDetailSerializer
from .modeldetail import SubsectionDetail, CategoryDetail, ProductDetail

# simple viewsets
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

# detail viewsets
class SubsectionDetailViewSet(viewsets.ModelViewSet):
        queryset = SubsectionDetail.objects.raw("SELECT * FROM shopapp_section JOIN shopapp_subsection ON Sid=shopapp_subsection.insection_id")
        permission_classes = [
                permissions.AllowAny
        ]
        serializer_class = SubsectionDetailSerializer

class CategoryDetailViewSet(viewsets.ModelViewSet):
        queryset = CategoryDetail.objects.raw("SELECT * FROM shopapp_section JOIN shopapp_subsection ON Sid=shopapp_subsection.insection_id JOIN shopapp_category ON shopapp_category.insubsection_id=Subid")
        permission_classes = [
                permissions.AllowAny
        ]
        serializer_class = CategoryDetailSerializer

class ProductDetailViewSet(viewsets.ModelViewSet):
        queryset = ProductDetail.objects.raw("SELECT * FROM shopapp_section JOIN shopapp_subsection ON Sid=shopapp_subsection.insection_id JOIN shopapp_category ON shopapp_category.insubsection_id=Subid JOIN shopapp_product ON shopapp_product.incategory_id=Cid")
        permission_classes = [
                permissions.AllowAny
        ]
        serializer_class = ProductDetailSerializer 
