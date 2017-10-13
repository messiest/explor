import uuid
from setuptools import setup
import os
from pip.req import parse_requirements

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
reqs_file = os.path.join(BASE_DIR, 'requirements.txt')
install_reqs = parse_requirements(reqs_file, session=uuid.uuid1())

setup(
    name="xplor",
    version="0.1",
    author="Christopher Messier",
    author_email="messiercr@gmail.com",
    description="Tool to automate exploratory data analysis",
    license="MIT",
    keywords="pandas data",
    install_requires=["numpy", "pandas", "seaborn", "matplotlib"],
    url="https://github.com/messiest/xplor",
    include_package_data=True,
    long_description=read('README.md')
)
