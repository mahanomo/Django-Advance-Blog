from django.forms import ModelForm
from .models import Post

# Create the form class.


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "status", "published_date"]
