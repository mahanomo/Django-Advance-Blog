from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","author","title","content","status","created_date","published_date"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = f"{instance.author.first_name} {instance.author.last_name}"
        return rep