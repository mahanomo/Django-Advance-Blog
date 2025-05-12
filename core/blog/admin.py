from django.contrib import admin
from .models import Post, Category


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "status", "created_date")
    list_filter = ("status", "created_date")


admin.site.register(Category)
