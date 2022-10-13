from django.urls import path
from rest_framework.routers import SimpleRouter

from images.views import ImageListViewset, ImageUploadView


router = SimpleRouter()
router.register('image', ImageListViewset)

urlpatterns = [
    path('uploadImage/', ImageUploadView.as_view())
]

urlpatterns += router.urls