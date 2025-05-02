from rest_framework import serializers
from blog.models import Post,Category

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url")
    class Meta:
        model = Post
        fields = ["id","author","title","content","status","snippet","relative_url","created_date","published_date"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = f"{instance.author.first_name} {instance.author.last_name}"
        return rep
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"]
