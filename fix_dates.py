
import os
import django
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afeeezsite.settings")
django.setup()

from blog.models import Post
from django.utils import timezone

# Hardcode a date in the past since the system clock is wrong.
PAST_DATE = timezone.make_aware(datetime(2023, 1, 1))

posts = Post.objects.all()

if not posts:
    print("No posts found to update.")
else:
    print(f"Found {len(posts)} posts. Updating publish dates...")
    for i, post in enumerate(posts):
        # Set publish dates descending from the hardcoded past date
        post.publish = PAST_DATE - timedelta(days=i)
        post.save()
        print(f"  - Updated '{post.title}' publish date to {post.publish}")
    print("\nUpdate complete.")
