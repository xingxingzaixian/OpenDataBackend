from django.urls import path
from rest_framework.routers import SimpleRouter

from dataset.views import StaticViewSet, RestViewSet, ScriptViewSet

router = SimpleRouter()
router.register('static', StaticViewSet)
router.register('rest', RestViewSet)
router.register('script', ScriptViewSet)

urlpatterns = [
]

urlpatterns += router.urls