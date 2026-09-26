from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scdns",
    version="1.0.0",
    author="Silent Cobra",
    author_email="********@gmail.com",
    description="Advanced DNS Lookup Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/silentcobrac4/scdns",
    packages=find_packages(),
    install_requires=[
        "dnspython",
        "requests",
        "rich",
        "colorama",
        "pyfiglet",
    ],
    entry_points={
        "console_scripts": [
            "scdns=dnslookup.dnsl_sc:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
