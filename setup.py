from setuptools import setup, find_packages

VERSION = '1.0.0'


setup(
    name="mkdocs-biojulia",
    version=VERSION,
    url='https://github.com/BioJulia/mkdocs-biojulia',
    license='MIT',
    description='',
    author='The BioJulia Organisation',
    author_email='axolotlfan9250@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'biojulia = biojulia',
        ]
    },
    zip_safe=False
)
