from django.test import TestCase
from datetime import datetime

from ..models import Post,Category
from accounts.models import User,Profile

class TestModel(TestCase):

    def setUp(self):
        self.category_obj = Category.objects.create(name="cat-test")
        self.user_obj = User.objects.create(email="admin@testttt.com",password="a/A@123456")
        self.profile = Profile.objects.create(
            user = self.user_obj,
            first_name = "mahan test",
            last_name = "mirdar test",
            descreaption = "bio for test"
        )
        
    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author = self.profile ,
            title = "title_test" ,
            content = "content_test" ,
            category = self.category_obj ,
            status = True ,
            published_date = datetime.now() ,
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual( post.title , "title_test" )


