from distutils.core import setup
from setuptools import setup

setup(
    name='pyflask',
    version='1.0',
    author='liuwill',
    author_email='liuwill@live.com',
    install_requires=[
        'flask>=0.12.1',
        'Flask-Cors>=3.0.2',
        'Jinja2>=2.9.6'
    ],
    #packages=['']
    #py_modules=['foo'],
    scripts=["server.py"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
