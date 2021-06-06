from django.urls import path, include
from blogging.views import stub_view, PostListView, PostDetailView, UserViewSet, PostViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [  # path('', stub_view, name = 'blog_index'),
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="blog_detail"),
    path("api/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace= 'rest_framework')),
]
