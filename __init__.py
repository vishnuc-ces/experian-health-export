from setuptools import setup

setup(
    name='experian-health-export',
    packages=['experian-health-export'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy'
    ],
)