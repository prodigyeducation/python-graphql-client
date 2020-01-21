"""Configuration for python project."""

from setuptools import setup

setup(
    name="python_graphql_client",
    version="0.1.0",
    description="Python GraphQL Client",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="api graphql client",
    url="https://github.com/SMARTeacher/python-graphql-client",  # TODO change this
    author="Justin Krinke",
    author_email="opensource@prodigygame.com",
    license="MIT",
    packages=["python_graphql_client"],
    install_requires=["aiohttp==3.6.2", "requests==2.22.0", "asynctest==0.13.0"],
    extras_require={
        "dev": ["pre-commit", "black", "flake8", "flake8-black", "flake8-isort"]
    },
)
