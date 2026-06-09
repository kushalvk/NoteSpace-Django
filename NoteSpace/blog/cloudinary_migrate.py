from blog.models import Post
from django.core.files import File
from django.conf import settings
import os

for post in Post.objects.exclude(image=""):
    local_path = os.path.join(settings.MEDIA_ROOT, post.image.name)

    if os.path.exists(local_path):
        with open(local_path, "rb") as f:
            post.image.save(post.image.name, File(f), save=True)
            print("Uploaded:", post.image.name)
    else:
        print("Missing:", local_path)

print("All Cloudinary uploads done")
