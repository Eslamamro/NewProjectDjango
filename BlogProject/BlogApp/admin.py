from django.contrib import admin
from .models import Profile, Post, Hashtag

class ProfilePost(admin.ModelAdmin):
    pass
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_date']
    list_filter = ['author', 'created_date']
    search_fields = ['title']
    ordering = ['-created_date']
    list_per_page = 5

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
admin.site.register(Hashtag)