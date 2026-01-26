from django.conf import settings

def supabase(request):
    return {
        "SUPABASE_URL": settings.SUPABASE_URL
    }
