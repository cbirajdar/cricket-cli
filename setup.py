from setuptools import setup

setup(
    name='cricket-cli',
    description='Command-line interface for cricket fans',
    version='1.0.0',
    packages=['cricket'],
    url='http://github.com/cbirajdar/cricket-cli',
    author='Chetan Birajdar',
    author_email='birajdar.chetan@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1.0.0 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: MIT',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.8',
        'Programming Language :: Python :: 2.9',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'grequests',
        'feedparser',
        'beautifulsoup4',
        'terminaltables'
    ],
    entry_points={
        "console_scripts": ['cricket = cricket.__main__:main'],
    }
)
