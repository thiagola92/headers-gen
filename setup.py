from setuptools import setup, find_packages

setup(
    name="headers_gen",
    version="0.0.1",
    author="thiagola92",
    packages=find_packages(exclude=["tests"]),
    install_requires=["packaging==21.3"],
)
