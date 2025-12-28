#!/usr/bin/env python
"""Setup configuration for imgdedup package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="duplicate-image-finder",
    version="0.1.0",
    author="Shailesh Suvarna",
    author_email="shaileshsuvarna24@gmail.com",
    description="A fast, offline CLI tool to find and remove visually duplicate images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shailesh7860/Delete-Duplicate-Images",
    py_modules=["imgdedup"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "duplicate-image-finder=imgdedup:main",
        ],
    },
)
