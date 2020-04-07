import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covidwrapper", # Replace with your own username
    version="0.0.1",
    author="Samuel Adekoya",
    author_email="damiloladrizzy@yahoo.com",
    description="A Python wrapper for the covid19 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/damildrizzy/pyvid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)