from django.contrib import admin

from clone.models import SocialPost

class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'likes']
    search_fields = ['user_id']

admin.site.register(SocialPost, PostsAdmin)

