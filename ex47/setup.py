try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Excercise 48 from Learn Python the Hard Way',
	'author': 'Gino Chiudioni',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'gtchiudi20@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'Exercise 48'
}

setup(**config)
