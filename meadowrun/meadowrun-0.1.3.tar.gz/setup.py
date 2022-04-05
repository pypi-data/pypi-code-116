# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['meadowrun',
 'meadowrun._vendor',
 'meadowrun._vendor.aiodocker',
 'meadowrun.aws_integration',
 'meadowrun.aws_integration.management_lambdas',
 'meadowrun.func_worker']

package_data = \
{'': ['*'], 'meadowrun': ['docker_files/*']}

install_requires = \
['aiobotocore>=2.1.2,<3.0.0',
 'aiohttp>=3.8.0,<4.0.0',
 'boto3==1.21.21',
 'cloudpickle>=2.0.0,<3.0.0',
 'fabric>=2.6.0,<3.0.0',
 'filelock>=3.6.0,<4.0.0',
 'pandas>=1.3.1,<2.0.0',
 'protobuf>=3.18.1,<4.0.0',
 'psutil>=5.8.0,<6.0.0',
 'typing-extensions>=4.1.1,<5.0.0']

entry_points = \
{'console_scripts': ['meadowrun-local = '
                     'meadowrun.run_job_local_main:command_line_main',
                     'meadowrun-manage = meadowrun.manage:main']}

setup_kwargs = {
    'name': 'meadowrun',
    'version': '0.1.3',
    'description': 'The easiest way to run python code on one or more remote machines',
    'long_description': None,
    'author': 'Richard Lee',
    'author_email': 'hrichardlee@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/meadowdata/meadowrun',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
