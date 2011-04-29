import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.markdown')

setup(
    name = "django-socialsharing",
    version = "0.1",
    description='Simple integration of social sharing widgets (such as AddThis) in Django projects.',
    url = 'http://github.com/lettertwo/django-socialsharing',
    license = 'BSD',
    long_description=README,

    author = 'Eric Eldredge',
    author_email = 'lettertwo@gmail.com',
    packages = [
        'socialsharing',
        'socialsharing.templates',
        'socialsharing.templatetags',
    ],
    package_data = {'socialsharing': ['templates/*', 'static/*']},
    requires = [],
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)