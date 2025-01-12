# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name="pyexiv2",
    version="1.2.2",
    author="LeoHsiao",
    author_email="leohsiao@foxmail.com",
    description="Read and modify metadata of digital image, including EXIF, IPTC, XMP.",
    long_description="See README",
    long_description_content_type="text/markdown",
    url="https://github.com/LeoHsiao1/pyexiv2",
    packages=setuptools.find_packages(),
    package_data ={"pyexiv2":["lib/*","tests/*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
)


# upload to pypi.org:
#   python setup.py sdist bdist_wheel
#   python -m twine upload dist/*
