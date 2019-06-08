from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sitesize',
    version='0.1',
    description='Getting size of web page',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Siddhant Shaw',
    author_email='siddhantshaw97@gmail.com',
    url='https://github.com/mianto/sitesize',
    license=license,
    packages=find_packages(exclude=('tests')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)