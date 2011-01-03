import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read( fname ):
    return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()

setup( name = 'magickwand',
       version = '0.2',
       description = '''Python bindings for ImageMagick's MagickWand 6.6.0''',
       long_description = read( 'README' ),
       keywords = "ImageMagick MagickWand CDLL Binding",
       author = 'Oliver Berger',
       author_email = 'oliver@digitalarchitekt.de',
       url = 'http://digitalarchitekt.de/contributions/magickwand',
       packages = find_packages( exclude = 'test' ),
       classifiers = [
                    "Development Status :: 3 - Alpha",
                    "Topic :: Multimedia :: Graphics",
                    ],
     )
