import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-pipelines-github",
    "version": "0.2.24",
    "description": "GitHub Workflows support for CDK Pipelines",
    "license": "Apache-2.0",
    "url": "https://github.com/cdklabs/cdk-pipelines-github.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdklabs/cdk-pipelines-github.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_pipelines_github",
        "cdk_pipelines_github._jsii"
    ],
    "package_data": {
        "cdk_pipelines_github._jsii": [
            "cdk-pipelines-github@0.2.24.jsii.tgz"
        ],
        "cdk_pipelines_github": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk-lib>=2.19.0, <3.0.0",
        "constructs>=10.0.46, <11.0.0",
        "jsii>=1.55.1, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
