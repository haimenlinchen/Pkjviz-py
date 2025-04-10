#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

if __name__ == "__main__":
    setup(
        name="pkjviz",
        version="0.1.0",
        description="Python implementation of Pkjviz",
        author="Author",
        packages=["pkjviz"],
        entry_points={
            "console_scripts": [
                "pkjviz=pkjviz.app.run:main",
            ],
        },
        install_requires=[
            "PyQt5>=5.15.0",
            "qtpy>=2.0.0",
            "qtawesome>=1.0.0",
        ],
        python_requires=">=3.8",
    ) 