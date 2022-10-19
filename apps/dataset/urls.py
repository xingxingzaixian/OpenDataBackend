from django.urls import path
from rest_framework.routers import SimpleRouter

from dataset.views import StaticViewSet, ResetViewSet, ScriptViewSet

router = SimpleRouter()
router.register('static', StaticViewSet)
router.register('reset', ResetViewSet)
router.register('script', ScriptViewSet)

urlpatterns = [
]

urlpatterns += router.urls