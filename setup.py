import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unity-packer-Hicesha",
    version="0.0.1",
    author="Shawn Hice",
    author_email="shawnhice@autodesk.com",
    description="A package for creating unitypackage files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: NONE PROVIDED ATM",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)