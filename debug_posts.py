import os
import django
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'afeeezsite.settings')
django.setup()

from blog.models import Post

def inspect_published_posts():
    """
    Inspects the posts returned by the custom 'published' manager.
    """
    print("--- Inspecting Post.published.all() ---")

    # The exact query from the view
    published_posts = Post.published.all()

    post_count = published_posts.count()
    print(f"Found {post_count} posts using Post.published.all()")

    if post_count > 0:
        print("\nDetails of published posts:")
        for post in published_posts:
            print(f"- Title: {post.title}")
            print(f"  Status: {post.status}")
            print(f"  Publish Date: {post.publish}")
            print(f"  Is publish date in the past? {post.publish < timezone.now()}")
    else:
        print("\nNo posts were returned by the query.")
        print("\n--- Checking all posts in the database for comparison ---")
        all_posts = Post.objects.all()
        all_post_count = all_posts.count()
        print(f"Found {all_post_count} total posts in the database.")
        if all_post_count > 0:
            for post in all_posts:
                print(f"- Title: {post.title}")
                print(f"  Status: {post.status}")
                print(f"  Publish Date: {post.publish}")
                print(f"  Is status 'published'? {post.status == 'published'}")

if __name__ == "__main__":
    inspect_published_posts()
