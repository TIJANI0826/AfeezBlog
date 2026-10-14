
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afeeezsite.settings")
django.setup()

from blog.models import Post
from django.utils import timezone

posts = Post.objects.all()

if not posts:
    print("No posts found in the database.")
else:
    print(f"Found {len(posts)} posts. Details:")
    for p in posts:
        print(f"  - Title: {p.title}")
        print(f"    Status: {p.status}")
        print(f"    Publish Date: {p.publish}")
        print(f"    Is in the past: {p.publish <= timezone.now()}")
        print("-" * 20)
