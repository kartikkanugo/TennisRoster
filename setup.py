from setuptools import setup, find_packages
from tennisroster import version
setup(
    name='tennisroster',
    version=version.__version__,
    packages=find_packages(exclude=['test']),
    url='',
    license='LICENSE.txt',
    author='kartik',
    author_email='karthik.kanugo@gmail.com',
    description='Tennis Roster system'
)
