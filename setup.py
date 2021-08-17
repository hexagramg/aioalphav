from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='aioalphav',
    version='0.0.1',
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.9, <4',
    package_dir={'': 'src'},
    url='https://github.com/hexagramg/aioalphav',
    license='GPL-3.9',
    author='hexagramg',
    author_email='hexagramg@gmail.com',
    description='Asynchronous alpha vantage wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['aiohttp']
)
