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
    long_description=read('README.md'))


from setuptools import setup, find_packages
setup(
    name="mTree",
    version="0.2-PRE",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Flask>=0.12',
                      'Flask-APScheduler>=1.7.0',
                      'Flask-BasicAuth>=0.2.0',
                      'Flask-Bootstrap>=3.3.7.1',
                      'Flask-SocketIO>=2.8.6',
                      'Flask-SQLAlchemy>=2.1',
                      'eventlet>=0.20.1',
                      'numpy>=1.11.1',
                      'PyYaml>=3.12'],

    # metadata for upload to PyPI
    author="GMU CSN",
    author_email="gmucsn@gmucsn.edu",
    description="This is the base mTree package",
    license="MIT",
    keywords="experimental economics",
    url="https://github.com/gmucsn/mTree",   # project home page, if any
)