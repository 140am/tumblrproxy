import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'pyramid==1.4',
    #'pyramid_debugtoolbar',
    'pyramid_exclog',
    'waitress',
    'nose',
    'coverage',
    'pyramid_jinja2',
    'pytumblr'
    ]

setup(name='tumblrproxy',
      version='0.1',
      description='Tumblr.com Blog Proxy',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='tumblrproxy',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tumblrproxy:main
      """,
      )
