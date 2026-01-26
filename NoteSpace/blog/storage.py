from .supabase import supabase
import uuid

def upload_to_supabase(file):
    filename = f"blog_images/{uuid.uuid4()}_{file.name}"
    supabase.storage.from_("notespace").upload(filename, file.read())
    return filename
