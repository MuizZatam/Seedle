from setuptools import setup, find_packages

setup(

    name="seedle",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "seedle=modules.cli:main",
        ],
    },
    description="A tool to simplify Python project creation and dependency management",
    author="Muiz Zatam",
    author_email="muizzatam110@gmail.com",
    python_requires=">=3.8",
)