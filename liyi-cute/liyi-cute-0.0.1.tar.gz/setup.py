#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 15:18
# @Author  : Yizheng Dai
# @Email   : 387942239@qq.com
# @File    : setup.py.py

import setuptools

__version__ = None
exec(open('liyi_cute/version.py').read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


tests_requires = [
    "pytest"
]

install_requires = [
    "spacy>=2.3.0,<2.4.0",
    "marshmallow >= 3.15.0",
    "transformers >= 4.17.0",
    "setuptools-scm >= 6.4.2",
    "seqeval[cpu] == 1.2.2"
]

extras_requires = {
    'test': tests_requires
}

package_data = {
        "liyi_cute": ["*.py","*.so"]
    }

setuptools.setup(
    name="liyi-cute",
    version=__version__,
    author="yizheng dai",
    author_email="387942239@qq.com",
    maintainer="yizheng dai",
    maintainer_email="387942239@qq.com",
    license='Apache 2.0',
    description="A text processing tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daiyizheng/liyi-cute",
    keywords="Text processing tools, including named entity recognition, "
                 "relation extraction, event extraction, and some statistical "
                 "and visualization functions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
    install_requires= install_requires,
    tests_require=tests_requires,
    python_requires='>=3.8',
    package_data=package_data,
    project_urls={
            'Bug Reports': 'https://github.com/daiyizheng/liyi-cute/issues',
            'Source': 'https://github.com/daiyizheng/liyi-cute',
        }
)