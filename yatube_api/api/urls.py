from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = 'api'

router_api_v1 = routers.DefaultRouter()
router_api_v1.register(r'posts', PostViewSet, basename='posts')
router_api_v1.register(r'groups', GroupViewSet, basename='groups')
router_api_v1.register(r'posts/(?P<post_id>\d+)/comments',
                       CommentViewSet, basename='comments')
router_api_v1.register(r'follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_api_v1.urls), name='api-v1'),
]
