from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # list your dependencies
    ],
    entry_points={
        'console_scripts': [
            'mytool = src.main:main',
        ],
    },
)
########################################################
from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # list your dependencies
    ],
    entry_points={
        'console_scripts': [
            'mytool = src.main:main',
        ],
    },
)
