try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'script to add and remove my extention from support queue',
    'author': 'Jason Hamilton',
    'url': 'https://github.com/laydros/fpbxfollowme',
    'download_url': 'Where to download',
    'author_email': 'jwh@laydros.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['fpbxfollowme'],
    'scripts': [],
    'name': 'fpbxfollowme'
 }

setup(**config)
