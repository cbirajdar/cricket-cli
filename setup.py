from setuptools import setup

setup(
    name='cricket-cli',
    description='Command-line interface for cricket fans',
    version='0.1',
    packages=['cricket'],
    url='http://github.com/cbirajdar/cricket-cli',
    author='Chetan Birajdar',
    author_email='birajdar.chetan@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: MIT'
    ],
    install_requires=[
        'grequests',
        'feedparser',
        'beautifulsoup4',
        'terminaltables',
        'colorclass'],
    entry_points={
        "console_scripts": ['cricket = cricket.__main__:main'],
    }
)
