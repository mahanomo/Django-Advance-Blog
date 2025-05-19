from django.core.management.base import BaseCommand

from faker import Faker
from datetime import datetime
import random

from accounts.models import User, Profile
from blog.models import Post, Category

category_list = Category.objects.all()
cat_list=[]
for cat in category_list:
    cat_list.append(cat.name)

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command,self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user_obj= User.objects.create_user(email=self.fake.email(), password="Abc@12345")
        profile_obj = Profile.objects.get(user=user_obj)
        profile_obj.first_name = self.fake.first_name()
        profile_obj.last_name = self.fake.last_name()
        profile_obj.descreaption = self.fake.paragraph(nb_sentences=1)
        profile_obj.save()
        for _ in range(2):
            Post.objects.create(
                author = Profile.objects.get(user=user_obj), 
                title = self.fake.paragraph(nb_sentences=1), 
                content = self.fake.paragraph(nb_sentences=9), 
                category = random.choice(category_list), 
                status = random.choice([True,False]), 
                published_date = datetime.now(), 
            )
