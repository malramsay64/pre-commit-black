from setuptools import setup

from version import __version__

setup(
    name='pre_commit_black',
    description='A pre_commit pacakge for black',
    version=__version__,
    install_requires=['black==' + str(__version__)],
)
