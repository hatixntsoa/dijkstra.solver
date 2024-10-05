from setuptools import setup, find_packages

setup(
    name='dijkstra-solver',
    version='0.1.0',
    description='A Python implementation of Dijkstra\'s algorithm for finding the shortest path in a weighted graph.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hatix Ntsoa',
    author_email='hatixntsoa@gmail.com',
    url='https://github.com/h471x/dijkstra_solver',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
)