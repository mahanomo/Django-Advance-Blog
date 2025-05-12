from django.test import TestCase,Client
from django.urls import reverse
from datetime import datetime

from ..models import Post,Category
from accounts.models import User,Profile

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.category_obj = Category.objects.create(name="cat-test")
        self.user_obj = User.objects.create(email="admin@testttt.com",password="a/A@123456")
        self.profile = Profile.objects.create(
            user = self.user_obj,
            first_name = "mahan test",
            last_name = "mirdar test",
            descreaption = "bio for test"
        )
        self.post = Post.objects.create(
            author = self.profile ,
            title = "title_test" ,
            content = "content_test" ,
            category = self.category_obj ,
            status = True ,
            published_date = datetime.now() ,
        )

    def test_blog_index_url_successful_response(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
        self.assertTrue(str(response.content).find('Home'))
        self.assertTemplateUsed(response, template_name="blog/index.html")

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user_obj)
        url = reverse('blog:post-detail',kwargs={"pk":self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
    
    def test_blog_post_detail_anonymouse_response(self):
        url = reverse('blog:post-detail',kwargs={"pk":self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code , 302)