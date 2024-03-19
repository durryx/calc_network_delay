from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='calc_network_delay',
    version='0.1.0',
    description='calculate packet delay given a topological description of the network',
    long_description=readme,
    author='Giovanni Durante, Pietro Foresta',
    author_email='giovanni3durante@gmail.com',
    url='',
    packages=find_packages(exclude=('test', 'docs')),
    install_requires=[

    ]
)
