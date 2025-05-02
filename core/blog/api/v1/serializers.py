from rest_framework import serializers
from blog.models import Post,Category
from accounts.models import Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"]


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url",read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")

    class Meta:
        model = Post
        fields = ["id","author","title","image","content","snippet","category","status","relative_url"
                  ,"absolute_url","created_date","published_date"]
        read_only_fields = ["author"]
    # for seperate list view and detial view for hide some field's in serializers
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        # in detial page
        if request.parser_context["kwargs"].get("pk"):
            rep.pop("snippet")
            rep.pop("relative_url")
            rep.pop("absolute_url")
        # and in list page
        else :
            rep.pop("content")

        # define author's name in list or detail page
        rep['author'] = f"{instance.author.first_name} {instance.author.last_name}"
        # define id and name of category in dict or json in list or detail page
        rep["category"] = CategorySerializer(instance.category,context={"request":request}).data
        return rep
    
    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def create(self,validated_data):
        validated_data["author"] = Profile.objects.get(user__id=self.context.get("request").user.id)
        return super().create(validated_data)