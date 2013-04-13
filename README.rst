====================
django-kittenstorage
====================
kittenstorage is a so called *development storage engine*.

Many people have the problem with gigantomanic production databases with 
gigabytes of pictures/files. It is a pain to keep the image files synchronised 
between development and production environments. 

Therefore I have written this storage engine. In case a file is not found, 
an image from placekitten.com_ will be used/displayed
instead.

If you are sick of kittens, you might want to check out django-dogstorage_ or django-apestorage_.

sorl-thumbnail users
====================

Note that newer versions of sorl-thumbnail have an integrated dummy engine, which
can load images from various dummy sources. This is super cool and I highly recommend
this over kittenstorage. Go and have a look at THUMBNAIL_DUMMY_.

The setting for placeholder kittens source would be:

    ``THUMBNAIL_DUMMY_SOURCE = http://placekitten.com/%(width)s/%(height)s``

or if you prefer grayscale:

    ``THUMBNAIL_DUMMY_SOURCE = http://placekitten.com/g/%(width)s/%(height)s``

Setup
=====
It's on pypi.

    ``pip install django-kittenstorage``

Feel free to clone from github too. Forking is welcome as well :-)

In your django settings file:

    ``DEFAULT_FILE_STORAGE = 'kittenstorage.storages.GreyKitten'``

Storage Engines
===============
kittenstorage offers two engines:

1. ``kittenstorage.storages.GreyKitten``
2. ``kittenstorage.storages.ColorKitten``

Choose depending on the saturation you want. I prefer ``GreyKitten`` since it 
does have a pretty classy look.

Settings
========
There is only one setting:

KITTEN_SIZE  
    Default: ``(1024, 1024)``

    A tuple of format `(width, height)`, specifiying the size of the image 
    requested from placekitten__.


.. _django-dogstorage: https://github.com/originell/django-dogstorage/
.. _django-apestorage: https://github.com/originell/django-apestorage/
.. _THUMBNAIL_DUMMY: http://sorl-thumbnail.readthedocs.org/en/latest/reference/settings.html#thumbnail-dummy
.. _placekitten.com: http://placekitten.com/
__ placekitten.com_

