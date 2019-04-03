from setuptools import setup

setup(
    name='pyusl',
    version='0.0.1',
    description='A package for calculating Universal Scalability Law (USL)',
    license='MIT',
    packages=['pyusl'],
    author='ChangQing Wang',
    author_email='wip727@gmail.com',
    keywords=['Scalability testing', 'Universal Scalability Law', 'USL'],
    url='https://github.com/wip727/PyUSL',
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy'
    ],
)
