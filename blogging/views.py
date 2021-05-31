from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def stub_view(request, *args, **kwargs):
    body = 'Stub View\n\n'
    if args:
        body += 'Args:\n'
        body += '\n'.join(['\t%s' % a for a in args])

    if kwargs:
        body += 'Kwargs:\n'
        body += '\n'.join(['\t%s: %s' % i for i in kwargs.items()])

    return HttpResponse(body, content_type='text\plain')

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
    queryset = Post.objects.order_by('-published_date').exclude(published_date__exact=None)
    template_name = 'blogging/list.html'

class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    print(queryset)
    template_name = 'blogging/detail.html'
