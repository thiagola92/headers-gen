from pathlib import Path
from setuptools import setup, find_packages

long_description = Path("README.md").read_text()

setup(
    name="la-headers",
    version="0.0.1",
    description="Headers generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagola92/la-headers",
    author="thiagola92",
    author_email="thiagola92@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="headers, request, browser",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=["packaging==21.3"],
    python_requires=">=3.10",
)
