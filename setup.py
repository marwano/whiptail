import re
from setuptools import setup

readme = open('README.rst').read()
changes = open('CHANGES.txt').read()
version_file = 'whiptail.py'
version = re.findall("__version__ = '(.*)'", open(version_file).read())[0]
try:
    version = __import__('utile').git_version(version)
except ImportError:
    pass

setup(
    name='whiptail',
    version=version,
    description="Use whiptail to display dialog boxes from shell scripts",
    long_description=readme + '\n\n' + changes,
    keywords='whiptail',
    author='Marwan Alsabbagh',
    author_email='marwan.alsabbagh@gmail.com',
    url='https://github.com/marwano/whiptail',
    license='BSD',
    py_modules=['whiptail'],
    namespace_packages=[],
    include_package_data=True,
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
