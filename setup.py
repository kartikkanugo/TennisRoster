from setuptools import setup
from roster import version
setup(
    name='TennisRoster',
    version=version.__version__,
    packages=['roster', 'roster.resources'],
    url='',
    license='LICENSE.txt',
    author='kartik',
    author_email='karthik.kanugo@gmail.com',
    description='Tennis Roster system',
    long_description=open('README.md').read()
)
