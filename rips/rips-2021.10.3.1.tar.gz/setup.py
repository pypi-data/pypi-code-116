from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
	license = f.read()

RIPS_DIST_VERSION = '1'
	
setup(
    name='rips',
    version='2021.10.3.' + RIPS_DIST_VERSION,
    description='Python Interface for ResInsight',
    long_description=readme,
    author='Ceetron Solutions',
    author_email='info@ceetronsolutions.com',
    url='http://www.resinsight.org',
    license=license,
    packages=['rips'],
    package_data={'rips': ['*.py', 'generated/*.py', 'PythonExamples/*.py', 'tests/*.py']},
    install_requires=['grpcio>=1.20.0', 'protobuf', 'wheel']
)
