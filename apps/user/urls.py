from django.urls import path
from rest_framework.routers import SimpleRouter

from user.views import UserViewSet, LoginView, RegisterView

router = SimpleRouter()
router.register('info', UserViewSet)

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view())
]

urlpatterns += router.urls