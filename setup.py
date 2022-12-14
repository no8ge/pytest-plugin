from setuptools import setup

setup(
    name='pytest-pusher',
    version='0.0.3',
    description='pytest plugin for push report to minio',
    long_description=open('README.md').read(),
    author='lunz1207',
    author_email='lunz1207@gmail.com',
    url='https://github.com/no8ge/pytest-pusher',
    packages=["pytest_pusher"],
    package_dir={"pytest_pusher": "src"},
    entry_points={"pytest11": [
        "pytest_pusher = pytest_pusher"]},
    setup_requires=['setuptools_scm'],
    install_requires=[
        'pytest>=3.6',
        'loguru==0.6.0',
        'minio==7.1.12'
    ],
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='pytest pytest report push',
    python_requires='>=3.0,  !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
