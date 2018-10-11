from setuptools import setup, find_packages

setup(
    name='Ktransfer2600',
    version='0.0.1',
    description="",
    author='Sam Schott',
    author_email='ss2151@cam.ac.uk',
    url='https://github.com/quaeritis/Ktransfer2600.git',
    license='MIT',
    long_description=open('README.md').read(),
    packages=find_packages(),
    package_data={
        'Ktransfer2600': ['*.ui']
    },
    entry_points={
        'console_scripts': [
            'Ktransfer2600=sweepVlist.__main__:main'
        ],
        'gui_scripts': [
            'Ktransfer2600_gui=sweepVlist.__main__:main'
        ]
    },
    install_requires=[
    ],
    zip_safe=False,
    keywords='Ktransfer2600',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=[
    ]
)
