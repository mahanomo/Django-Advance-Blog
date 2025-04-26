from django.db import models
# from django.contrib.auth import get_user_model

#define in the app user for authorization
# User = get_user_model()
# Create your models here.
class Post(models.Model):
    '''
    create Post model for blog app
    '''
    author = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category',null=True,on_delete=models.SET_NULL)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name