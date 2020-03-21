from django.contrib import admin
from .models import Post #import the schema

#To make model visible on admin page
admin.site.register(Post)