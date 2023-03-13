from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'status', StatusViewSet, basename='user_status')

status_router = routers.NestedSimpleRouter(user_router, r'status', lookup='user_status')
status_router.register(r'comments', CommentViewSet, basename='comment')
status_router.register(r'reactions', ReactionViewSet, basename='reaction')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(user_router.urls)),
    path(r'', include(status_router.urls)),
]