import codecs
import os

from setuptools import find_packages, setup


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="maze_runner",
    packages=find_packages(),
    version=read("VERSION"),
    license="MIT License",
    # install_requires=[],
    # requires=[],
    # classifiers=[],
    description="Programming challenge for CS students.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Matheus Jardim Bernardes",
    author_email="matheusjardimb@gmail.com",
    maintainer="Matheus Jardim Bernardes",
    maintainer_email="matheusjardimb@gmail.com",
    url="https://github.com/matheusjardimb/maze_runner/",
    download_url="https://github.com/matheusjardimb/maze_runner/zipball/main",
)
