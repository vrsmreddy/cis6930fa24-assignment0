
from setuptools import setup, find_packages

setup(
    name='assignment0',
    version='1.0',
    author='Rama Satyanarayana Murthy Reddy Velagala',
    author_email='r.velagala@ufl.edu',
    description='A description of your project',
   
    
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


