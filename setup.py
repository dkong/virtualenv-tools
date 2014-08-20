import os
from setuptools import setup

readme = open(os.path.join(os.path.dirname(__file__), 'README'), 'r').read()

setup(
    name='virtualenv-tools',
    author='Fireteam Ltd.',
    author_email='support@fireteam.net',
    version='1.0-1',
    url='https://github.com/Wikia/virtualenv-tools',
    py_modules=['virtualenv_tools'],
    description='Tools for dealing with virtualenvs for code deployments (fork).',
    long_description=readme,
    entry_points={
        'console_scripts': [
            'virtualenv-tools = virtualenv_tools:main'
        ]
    },
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)
