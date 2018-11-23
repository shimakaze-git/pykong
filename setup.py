from setuptools import setup
# from setuptools import find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pykong',
    version='0.0.1',
    description='pykong is a python client library of Kong',
    long_description=readme,
    author='shimakaze.soft / shimakaze-git',
    author_email='',
    url='https://github.com/shimakaze-git/pykong',
    license=license,
    # packages=find_packages(exclude=('tests', 'docs')),
    packages=['pykong', 'cli'],
    entry_points={
        'console_scripts': [
            'pykong = cli.pykong_cli:main'
        ],
    },
    install_requires=[
        'click',
        'requests',
        'simplejson',
        'PyYAML'
    ],
    dependency_links=[]
)
