from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .models import Post
from .forms import PostForm

# Create your views here.


class IndexView(TemplateView):
    paginate_by = 2
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context["title"] = "Home"
        return context


class PostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/list_view.html"
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(status=True).order_by("-id")


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class AuthorCreateView(LoginRequiredMixin, CreateView):
    template_name = "blog/post_form.html"
    form_class = PostForm
    success_url = "/blog/posts/"

    def form_valid(self, form):
        # Attach the currently logged-in user as the author before saving
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/posts/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/posts/"
