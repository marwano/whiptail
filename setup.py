import os
import re
from setuptools import setup

README = open('README.rst').read()
CHANGES = open('CHANGES.txt').read()
VERSION = re.findall("__version__ = '(.*)'", open('whiptail.py').read())[0]

setup(
    name='whiptail',
    version=VERSION,
    description="Collection of useful functions and classes",
    long_description=README + '\n\n' + CHANGES,
    keywords='whiptail',
    author='Marwan Alsabbagh',
    author_email='marwan.alsabbagh@gmail.com',
    url='https://github.com/marwano/whiptail',
    license='BSD',
    py_modules=['whiptail'],
    namespace_packages=[],
    include_package_data=True,
    install_requires=['utile>=0.1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
