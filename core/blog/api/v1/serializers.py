from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["id","author","title","content","status","created_date","published_date"]

    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    