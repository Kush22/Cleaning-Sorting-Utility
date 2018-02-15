from setuptools import setup, find_packages
from os import path
from codecs import open

# Getting the path to the current directory
here = path.abspath(path.dirname(__file__))

# Getting the long description form the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='InnoCleaner',

    version='1.0.0.1',

    # packages=['venv.lib.python3.5.distutils', 'venv.lib.python3.5.encodings', 'venv.lib.python3.5.importlib',
    #           'venv.lib.python3.5.collections', 'venv.lib.python3.5.site-packages.pip',
    #           'venv.lib.python3.5.site-packages.pip.req', 'venv.lib.python3.5.site-packages.pip.vcs',
    #           'venv.lib.python3.5.site-packages.pip.utils', 'venv.lib.python3.5.site-packages.pip.compat',
    #           'venv.lib.python3.5.site-packages.pip.models', 'venv.lib.python3.5.site-packages.pip._vendor',
    #           'venv.lib.python3.5.site-packages.pip._vendor.distlib',
    #           'venv.lib.python3.5.site-packages.pip._vendor.distlib._backport',
    #           'venv.lib.python3.5.site-packages.pip._vendor.colorama',
    #           'venv.lib.python3.5.site-packages.pip._vendor.html5lib',
    #           'venv.lib.python3.5.site-packages.pip._vendor.html5lib._trie',
    #           'venv.lib.python3.5.site-packages.pip._vendor.html5lib.filters',
    #           'venv.lib.python3.5.site-packages.pip._vendor.html5lib.treewalkers',
    #           'venv.lib.python3.5.site-packages.pip._vendor.html5lib.treeadapters',
    #           'venv.lib.python3.5.site-packages.pip._vendor.html5lib.treebuilders',
    #           'venv.lib.python3.5.site-packages.pip._vendor.lockfile',
    #           'venv.lib.python3.5.site-packages.pip._vendor.progress',
    #           'venv.lib.python3.5.site-packages.pip._vendor.requests',
    #           'venv.lib.python3.5.site-packages.pip._vendor.requests.packages',
    #           'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.chardet',
    #           'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3',
    #           'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3.util',
    #           'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3.contrib',
    #           'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3.packages',
    #           'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
    #           'venv.lib.python3.5.site-packages.pip._vendor.packaging',
    #           'venv.lib.python3.5.site-packages.pip._vendor.cachecontrol',
    #           'venv.lib.python3.5.site-packages.pip._vendor.cachecontrol.caches',
    #           'venv.lib.python3.5.site-packages.pip._vendor.webencodings',
    #           'venv.lib.python3.5.site-packages.pip._vendor.pkg_resources',
    #           'venv.lib.python3.5.site-packages.pip.commands', 'venv.lib.python3.5.site-packages.pip.operations',
    #           'venv.lib.python3.5.site-packages.click', 'venv.lib.python3.5.site-packages.wheel',
    #           'venv.lib.python3.5.site-packages.wheel.test',
    #           'venv.lib.python3.5.site-packages.wheel.test.simple.dist.simpledist',
    #           'venv.lib.python3.5.site-packages.wheel.test.complex-dist.complexdist',
    #           'venv.lib.python3.5.site-packages.wheel.tool', 'venv.lib.python3.5.site-packages.wheel.signatures',
    #           'venv.lib.python3.5.site-packages.setuptools', 'venv.lib.python3.5.site-packages.setuptools.extern',
    #           'venv.lib.python3.5.site-packages.setuptools.command', 'venv.lib.python3.5.site-packages.pkg_resources',
    #           'venv.lib.python3.5.site-packages.pkg_resources.extern',
    #           'venv.lib.python3.5.site-packages.pkg_resources._vendor',
    #           'venv.lib.python3.5.site-packages.pkg_resources._vendor.packaging'],

    url='https://kush22.github.io/Cleaning-Sorting-Utility/',

    license='MIT LICENSE',

    author='Kushagra Gupta',

    author_email='kushagra.gupta@students.iiit.ac.in',

    description='This is a CLI based cleaner utility for Unix based systems.',

    long_description=long_description,

    # long_description='A CLI Based cleaner which has functionality to scan the file system to find the specified'
    #                  'number of files that have the largest size. The utility is Unix Based for now.'
    #                  '\n1.This is displayed as a list of files and various '
    #                  'other options to compress/delete the files are provided. '
    #                  '\n2.Space saving stats are displayed with each cleaning action'
    #                  '\n3.Duplicate files are detected recursively for each folder from the path that is spceified'
    #                  '\n4.Cleanup of the temporary file is also provided. '
    #                   'For that root-user permissions are necessary',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Cleaning Tools :: Python CLI Tool',

        'License :: MIT License',

        # Right now python 2 not supported
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Cleaning Utility Python-Tools',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    entry_points={
        'console_scripts': [
            'cleaningUtility=cleaningUtility:main'
        ],
    },

)
