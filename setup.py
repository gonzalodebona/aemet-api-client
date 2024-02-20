from setuptools import setup, find_packages

setup(
    name="aemet-api-client",
    version="0.2.0",
    description="Client for the Aemet API",
    author="Gonzalo de Bona",
    author_email="debonagonzalo@gmail.com",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3.8"],
    install_requires=[
        'requests>=2.26.0',
        'pytest>=7.2.2',
        'pytz~=2024.1',
        'pytest>=7.2.2',
        'setuptools~=68.2.2',
        'pandas>=1.3.3',
        'numpy>=1.21.2'
    ]
)
