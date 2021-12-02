from django.contrib import admin
from .models import Post, templateImages, Comment


admin.site.register(Post)
admin.site.register(templateImages)
admin.site.register(Comment)