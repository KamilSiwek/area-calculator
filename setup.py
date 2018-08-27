import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="area_calculator_codepany",
    version="0.0.1",
    author="Codepany",
    author_email="contact@codepany.com",
    description="Package to: calculate area and circumference points of takes location; calculate distance betweet points of takes location; checking if the point is in a given area. Package having regard to the earth model (default WGS84)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codepany/area-calculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
