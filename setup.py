from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sitesize',
    version='1.0',
    description='Getting size of web page',
    long_description=readme,
    author='Siddhant Shaw',
    author_email='siddhantshaw97@gmail.com',
    url='https://github.com/mianto/sitesize',
    license=license,
    packages=find_packages(exclude=('tests'))
)