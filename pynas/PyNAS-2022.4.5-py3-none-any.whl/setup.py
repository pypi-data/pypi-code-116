import os, shutil
from setuptools import setup
from config import version

#移除构建的build文件夹
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CUR_PATH, "build")
if os.path.isdir(path):
    print("del dir ", path)
    shutil.rmtree(path)

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
            print(os.path.join('..', path, filename))
    return paths

extra_files = package_files('static') + package_files('templates')

with open("requirements.txt", "r",encoding="utf-8") as f:
    requires = f.read()
    requires = requires.split("\n")


setup(
    name = "PyNAS",
    author_email="issues@wufan.fun",
    author = "Fan Wu",
    description="Python NAS, Based On Updog.",
    keywords="NAS Netdisk Flask Login ConfFile",
    url="http://wufan.fun/",
    project_urls={
        "Source Code": "https://gitee.com/shwufan/nas/",
    },
    version = version,
    package_dir ={"": "."},
    package_data = {'': extra_files},
    entry_points={
        "console_scripts": [
            "nas = main:main",
            "nas-gui = main_gui:main"
        ]
    },
    include_package_data=True,
    install_requires=requires,
    tests_require=[
        'pytest>=3.3.1',
        'pytest-cov>=2.5.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Customer Service',
        'License :: OSI Approved :: MIT License',
        'Framework :: Flask',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        # 'Programming Language :: Python :: 3.10',
        # 'Programming Language :: Python :: 3.11',
    ],
    long_description=open("README.rst", encoding="utf-8").read(),
)