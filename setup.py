from setuptools import setup

install_requires = [
    "grequests==0.3.0",
    "feedparser==5.2.1",
    "beautifulsoup4==4.6.0",
    "terminaltables==3.1.0"
]

setup(
    name='cricket-cli',
    description='Command-line interface for cricket enthusiasts',
    long_description=open('README.rst').read(),
    version='1.0.0b2',
    packages=['cricket'],
    url='http://github.com/cbirajdar/cricket-cli',
    author='Chetan Birajdar',
    author_email='birajdar.chetan@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=install_requires,
    entry_points={
        "console_scripts": ['cricket = cricket.__main__:main'],
    }
)
