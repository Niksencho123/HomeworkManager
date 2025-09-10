from django.conf import settings

def admin_media(request):
    return {'VERSION': settings.VERSION}