import setuptools
from distutils.core import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='quadratic-sieve',
    packages=['quadratic_sieve'],
    version='0.1.3',
    description='A basic implementation of the quadratic sieve factorization.',
    author='Mikolaj Sawicki',
    author_email='msawicki9999@gmail.com',
    license='GNU General Public License v3.0',
    scripts=['bin/quadratic_sieve'],
    url='https://github.com/mikolajsawicki/quadratic-sieve',
    long_description=long_description,
    install_requires=['numpy', ],
    download_url='https://github.com/cocojambo320/quadratic-sieve',
    keywords=['factorization', 'prime', 'number', 'theory', 'quadratic', 'sieve'],
    python_requires='>=3.7',
    setup_requires=['wheel'],
    long_description_content_type="text/markdown",
    include_package_data=True,
)
