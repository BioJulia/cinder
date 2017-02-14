from setuptools import setup, find_packages

setup(
    name = 'mkdocs-biojulia',
    packages = find_packages(),
    version = '1.0.1',
    description='Mkdocs Cinder theme customised for BioJulia.',
    author='The BioJulia Organisation',
    author_email='Ward9250@gmail.com',
    url = 'https://github.com/BioJulia/mkdocs-biojulia',
    license='MIT',
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'biojulia = biojulia',
        ]
    },
    zip_safe=False
)
