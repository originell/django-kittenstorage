import tempfile
import urllib2

from django.core.cache import cache
from django.core.files import File
from django.core.files.storage import FileSystemStorage

from kittenstorage.settings import KITTEN_SIZE


class ColorKitten(FileSystemStorage):
    """
    If a file is not found on disk, return a kitten picture.
    """
    def _open(self, name, mode='rb'):
        if not self.exists(name):
            kittenz = cache.get('kittenz', False)
            if not kittenz:
                # Grab a kitten from placekitten.
                response = urllib2.urlopen('http://placekitten.com/%s/%s'
                                           % (KITTEN_SIZE[0], KITTEN_SIZE[1]))
                kitten_img = response.read()
                cache.set('kittenz', kitten_img)
                kitten = tempfile.TemporaryFile()
                kitten.write(kitten_img)
                # .write places the readhead at the end. Resetting it
                # to the start, otherwise an empty File() will be created.
                kitten.seek(0)
                return File(kitten)
            else:
                past_kitten = tempfile.TemporaryFile()
                past_kitten.write(kittenz)
                past_kitten.seek(0)
                return File(past_kitten)
        return super(ColorKitten, self)._open(name, mode)

