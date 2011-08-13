# django-kittenstorage
kittenstorage is a so called _development storage engine_.

Many people have the problem with gigantomanic production databases with 
gigabytes of pictures/files. It is a pain to keep the image files synchronised 
between development and production environments.  
Therefore I have written this storage engine. In case a file is not found, 
an image from [placekitten.com](http://placekitten.com/) will be used/displayed
instead.

# Setup
It's on pypi.

    pip install django-kittenstorage

Feel free to clone from github too. Forking is welcome as well :-)

# Storage Engines
kittenstorage offers two engines:

1. `kittenstorage.storages.GreyKitten`
2. `kittenstorage.storages.ColorKitten`

Choose depending on the saturation you want. I prefer `GreyKitten` since it 
does have a pretty classy look.

# Settings
There is only one setting:

* KITTEN\_SIZE  
  Default: `(1024, 1024)`  
  A tuple of format `(width, height)`, specifiying the size of the image 
  requested from placekitten.
