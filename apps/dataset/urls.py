from django.urls import path
from rest_framework.routers import SimpleRouter

from dataset.views import StaticViewSet

router = SimpleRouter()
router.register('static', StaticViewSet)

urlpatterns = [
]

urlpatterns += router.urls