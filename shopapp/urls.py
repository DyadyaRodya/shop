from rest_framework import routers
from .api import ProductViewSet, CategoryViewSet, SubsectionViewSet, SectionViewSet
from .api import SubsectionDetailViewSet, CategoryDetailViewSet, ProductDetailViewSet

router = routers.DefaultRouter()
router.register('api/shopapp/product', ProductViewSet, 'product')
router.register('api/shopapp/category', CategoryViewSet, 'category')
router.register('api/shopapp/subsection', SubsectionViewSet, 'subsection')
router.register('api/shopapp/section', SectionViewSet, 'section')
router.register('api/shopapp/subsectiondetail', SubsectionDetailViewSet, 'subsectiondetail')
router.register('api/shopapp/categorydetail', CategoryDetailViewSet, 'categorydetail')
router.register('api/shopapp/productdetail', ProductDetailViewSet, 'productdetail')

urlpatterns = router.urls