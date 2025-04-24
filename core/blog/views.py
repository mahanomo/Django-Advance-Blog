from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class IndexView(TemplateView):
    paginate_by = 2
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['title'] = "Home"
        return context
    
class PostsListView(ListView):
    model = Post
    template_name = "blog/list_view.html"
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(status=True).order_by("-id")
    
class PostDetailView(DetailView):
    model = Post

class AuthorCreateView(CreateView):
    model = Post
    fields = ["author", "title", "content", "published_date"]
    success_url = "/blog/posts/"