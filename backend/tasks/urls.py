from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, login_view, logout_view, Test1, UserViewSet


router = DefaultRouter()

router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'test', Test1, basename='test')
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
