#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['keytotext']

package_data = \
{'': ['*']}

install_requires = \
['torch',
 'transformers',
 'sentencepiece',
 'wandb',
 'pytorch_lightning',
 'datasets',
 'huggingface_hub',
 'keybert']

setup(name='keytotext',
      version='2.2.0',
      description='Text Generation Using Keywords',
      author='Gagan Bhatia',
      author_email='gbhatia880@gmail.com',
      url='https://github.com/gagan3012/keytotext',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='>=3.7',
     )
