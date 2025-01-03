from setuptools import setup, find_packages

setup(
    name="my_package",
    version="1.0.0",
    description="A package to calculate dimensions of objects in an image using OpenCV.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ojas Varshney",
    author_email="ojas@dkgrouplabs.com",
    url="https://github.com/yourusername/my_package",  # Update with your GitHub repo URL
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "opencv-python",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
