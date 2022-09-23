""" library setup """
from setuptools import setup


def readme():
    """ print long description """
    with open('README.md', encoding='utf-8') as f:
        long_descrip = f.read()
    return long_descrip


setup(
    name='pyhrmos',
    version='0.1',
    description='',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Kensuke Shimoji',
    author_email='k.zimoc@gmail.com',
    keywords=['hrmos'],
    packages=['pyhrmos'],
    install_requires=[
        'requests>=2.28.1'
    ]
)
