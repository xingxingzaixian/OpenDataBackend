# -*- coding: utf-8 -*-
""" 
@author: xingxingzaixian
@create: 2020/9/6
@description: 
"""
from django.urls import path
from rest_framework.routers import SimpleRouter

from page.views import PageViewset, PageGroupViewset, UploadPageView

router = SimpleRouter()
router.register('page', PageViewset)
router.register('page_group', PageGroupViewset)

urlpatterns = [
    path('uploadPage/', UploadPageView.as_view())
]

urlpatterns += router.urls
