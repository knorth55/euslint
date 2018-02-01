from setuptools import find_packages
from setuptools import setup


version = '1.0.0'


setup(
    name='euslint',
    version=version,
    packages=find_packages(),
    scripts=['bin/euslint'],
    install_requires=['argparse'],
    description='Linter for euslisp',
    long_description=open('README.md').read(),
    author='Shingo Kitagawa',
    author_email='shingogo.5511@gmail.com',
    url='https://github.com/knorth55/euslint',
    license='MIT',
    keywords='linter'
)
