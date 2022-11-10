import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TriCount",
    version="1.9.4",
    author="Chuen Zhang Lee",
    author_email="Chuen.Lee@uea.ac.uk",
    description="A python package for counting number of beetles in an image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chuen-Lee/TriCount",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ),
)
