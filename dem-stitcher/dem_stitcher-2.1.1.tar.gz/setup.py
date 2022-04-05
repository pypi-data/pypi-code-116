from pathlib import Path

from setuptools import find_packages, setup


setup(
    name='dem_stitcher',
    use_scm_version=True,
    description='Download and merge DEM tiles for processing interferograms with ISCE2.',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',

    url='https://github.com/ACCESS-Cloud-Based-InSAR/dem_stitcher',

    author='Charlie Marshak, David Bekaert, Michael Denbina, Marc Simard',
    author_email='charlie.z.marshak@jpl.nasa.gov',

    keywords='dem',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    python_requires='>=3.7',

    install_requires=[
        'affine',
        'boto3',
        'fiona',
        'gdal',
        'geopandas',
        'importlib_metadata',  # drop when py>=3.8
        'numpy',
        'pyproj',
        'rasterio',
        'requests',
        'shapely',
        'tqdm',
    ],

    extras_require={
        'develop': [
            'flake8',
            'flake8-import-order',
            'flake8-blind-except',
            'flake8-builtins',
            'pytest',
            'pytest-cov',
        ]
    },

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,
)
