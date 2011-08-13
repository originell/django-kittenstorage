from django.conf import settings

KITTEN_SIZE = getattr(settings, 'KITTEN_SIZE', (1024, 1024))
