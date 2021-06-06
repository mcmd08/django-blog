from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from blogging.serializers import UserSerializer, PostSerializer, CategorySerializer

# Create your views here.
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])

    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])

    return HttpResponse(body, content_type="text\plain")


# Function-based views
# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     # template = loader.get_template('blogging/list.html')
#     # print('posts dct is', posts)
#     # print('template is', template)
#     context = {'posts': posts}
#     # print('context is', context)
#     # body = template.render(context)
#     # print('body is', body)
#     # return HttpResponse(body, content_type='text/html')
#     return render(request, 'blogging/list.html', context)

# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     print('request is', request)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     print('context is', context)
#     print('request is', request)
#     return render(request, 'blogging/detail.html', context)

# Class-based views
class PostListView(ListView):
    model = Post
    queryset = Post.objects.order_by("-published_date").exclude(
        published_date__exact=None
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    # print(queryset)
    template_name = "blogging/detail.html"

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited"""
    model = Post
    queryset = Post.objects.order_by('-published_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint that allows categories to be viewed or edited"""
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]