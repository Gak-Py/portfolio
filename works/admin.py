from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Postモデルをadminページで見えるようにするため
#superuserを作る

# Register your models here.
