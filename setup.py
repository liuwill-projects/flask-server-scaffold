from distutils.core import setup
from setuptools import setup

setup(
    name='pyflask',
    version='1.0',
    author='liuwill',
    author_email='liuwill@live.com',
    url='http://www.liuwill.com',
    install_requires=[
        'flask>=0.12.1',
        'Flask-SocketIO>=2.8.6',
        'Flask-Cors>=3.0.2',
        'Jinja2>=2.9.6'
    ],
    packages=["chat"],
    #packages=['']
    #py_modules=['foo'],
    scripts=["main.py"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
