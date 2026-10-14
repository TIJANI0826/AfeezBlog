import datetime
from blog.models import Post
from django.utils import timezone

# A date in the past
past_date = timezone.now() - datetime.timedelta(days=10)

posts = Post.objects.all()
for post in posts:
    post.publish = past_date
    post.save()

print("Updated publish date for all posts to the past.")
