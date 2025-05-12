from django.test import TestCase
from datetime import datetime

from ..forms import PostForm

class TestForm(TestCase):
    def test_post_form_with_valid_data(self):
        form = PostForm(data={"title":"this is test title", "content":"and this is test content",
                               "status":True, "published_date":datetime.now()})
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())