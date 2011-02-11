from setuptools import setup, find_packages

setup(
    name = "django-template-preprocessor",
    version = "0.1",
    url = 'https://github.com/citylive/django-template-preprocessor',
    license = 'BSD',
    description = "Template preprocessor/compiler for Django",
    long_description = open('README.rst','r').read(),
    author = 'Jonathan Slenders, City Live nv',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = listify('requirements.pip'),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Topic :: Software Development :: Internationalization',
    ],
)
