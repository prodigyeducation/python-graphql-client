"""Configuration for python project."""

from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="python_graphql_client",
    version="0.4.3",
    description="Python GraphQL Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    url="https://github.com/prodigyeducation/python-graphql-client",
    author="Justin Krinke",
    author_email="opensource@prodigygame.com",
    license="MIT",
    packages=["python_graphql_client"],
    install_requires=["aiohttp~=3.0", "requests~=2.0", "websockets>=5.0"],
    extras_require={
        "dev": [
            "pre-commit",
            "black",
            "flake8",
            "flake8-docstrings",
            "flake8-black",
            "flake8-isort",
            "gitchangelog",
            "pystache",
        ]
    },
)
