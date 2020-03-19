import setuptools

with open("altTools/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="altTools",
    version="0.0.8",
    author="Ireoluwa Raufu",
    description="A collection of unrelated but useful Python functions in a single module. (Unstable Release)",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MasterGlasses76/altTools",
    keywords = ['useful', 'random', 'utility'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
