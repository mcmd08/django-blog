from django.urls import path, include
from blogging.views import stub_view, PostListView, PostDetailView
from rest_framework import routers

urlpatterns = [  # path('', stub_view, name = 'blog_index'),
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="blog_detail"),
    path("api/", include(routers.urls)),
    path("api-auth/", include('rest_framework.urls', namespace= 'rest_framework')),
]
