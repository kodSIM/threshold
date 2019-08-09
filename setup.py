from setuptools import setup, find_packages


setup(
    name='threshold',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pandas',
    ],
    entry_points='''
        [console_scripts]
        threshold=threshold.threshold:threshold
    ''',
    author='Smolnikov I.M.',
    description='Find and print critical values for CPU and memory usage for test.'
)
