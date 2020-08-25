from rest_framework import routers
from .api import ProductViewSet, CategoryViewSet, SubsectionViewSet, SectionViewSet, FullinfoViewSet

router = routers.DefaultRouter()
router.register('api/shopapp/product', ProductViewSet, 'product')
router.register('api/shopapp/category', CategoryViewSet, 'category')
router.register('api/shopapp/subsection', SubsectionViewSet, 'subsection')
router.register('api/shopapp/section', SectionViewSet, 'section')
router.register('api/shopapp/fullproduct', FullinfoViewSet, 'fullproduct')

urlpatterns = router.urls
