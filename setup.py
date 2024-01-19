from setuptools import setup, find_packages

setup(
    name="logbox",
    version="0.1.0",
    description="A simple Python package for making box for the string",
    package_dir={"": "logbox"},
    packages=find_packages(where="logbox"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)