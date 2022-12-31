# Always prefer setuptools over distutils
import pathlib
from setuptools import setup, find_packages

import numpy as np


here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='python-sorter',
    version='1.2.0',
    description='Apply multiple type of sorting algorithm on your data and also compare which sorting is fastes on your data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    author="Deep Dey",
    author_email='deepdey10998@gmail.com',
    url='https://github.com/Deep-Dey/python-sorter',
    keywords='sorting python buublesort quicksort mergesort',
    include_package_data=True,
    packages=find_packages(where='src', include=('*', 'data_sorter.*')),
    install_requires=[
        'numpy>=1.20',
        'pandas>=1.3',
        'seaborn>=0.11',
    ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3 :: Only",
    ],
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={"": "src"},  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    # packages=find_packages(where="src"),  # Required
)