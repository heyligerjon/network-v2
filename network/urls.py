from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'status', StatusViewSet, basename='user-status')
# router.register(r'users', CommentViewSet, basename='comment')
# router.register(r'users', ReactionViewSet, basename='reaction')
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(user_router.urls)),
]