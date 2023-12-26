from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='IYP',
    version='0.0.1',
    description="IYP AS INFO",
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Rishi Mondal',
    author_email='mavrickrishi@gmail.com',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'neo4j',
        'pandas',
        ]
)