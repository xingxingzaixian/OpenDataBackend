"""xingxing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.views.static import serve
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('docs/json/', SpectacularJSONAPIView.as_view(), name='schema'),
    # Optional UI:
    path('docs/ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('interface/', include('interface.urls')),
    path('user/', include('user.urls')),
    path('page/', include('page.urls')),
    path('image/', include('images.urls')),
    path('dataset/', include('dataset.urls'))
]

# 生产环境中使 API 文档也可访问
if not settings.DEBUG:
    urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})]