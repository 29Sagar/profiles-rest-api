from django.urls import path,include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename = 'hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
