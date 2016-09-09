from os.path import join, dirname
import setuptools


def read(fname):
    with open(join(dirname(__file__), fname)) as f:
        return f.read()

setuptools.setup(
    name="metallic-spectacles",
    version="0.0.1",
    author="Tony Fast",
    author_email="tony.fast@gmail.com",
    description="Simple reusable magics.",
    license="BSD-3-Clause",
    keywords="IPython Magic Jupyter",
    url="https://github.com/tonyfast/metallic-spectacles",
    packages=setuptools.find_packages(),
    long_description=read("readme.rst"),
    classifiers=[
        "Topic :: Utilities",
        "Framework :: IPython",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Testing",
    ],
    install_requires=[
        "scikit-learn", "whatever-forever",
    ]
)
