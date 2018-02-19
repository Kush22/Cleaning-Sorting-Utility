from setuptools import setup, find_packages
from os import path
from codecs import open

# Getting the path to the current directory
here = path.abspath(path.dirname(__file__))

# Getting the long description form the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='InnoCleaner',

    version='1.0.17.dev1',

    url='https://github.com/Kush22/Cleaning-Sorting-Utility',

    license='MIT LICENSE',

    author='Kushagra Gupta',

    author_email='kushagra.gupta@students.iiit.ac.in',

    description='This is a CLI based cleaner utility for Unix based systems.',

    long_description=long_description,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='Cleaning Utility Python-Tools',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['pathlib2'],

    python_requires='>2.7',

    entry_points={
        'console_scripts': [
            'InnoCleaner=InnoCleaner:main',
        ],
    },
)
