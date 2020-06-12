from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='hello_viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello', views.HelloApi.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
