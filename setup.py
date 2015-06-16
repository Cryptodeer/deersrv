"""
deersrv
==============

"""

from setuptools import setup, find_packages

setup(
    name='deersrv',
    version='0.8.3',
    url='https://github.com/assinnata/deerconsole',
    license='MIT',
    author='Matteo Assinnata',
    author_email='matteo@assinnata.com',
    description=("deerapi server"),
    keywords='Tetra Cryptodeer cryptocurrency',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'commontools==0.1.0',
        'ecdsa==0.11',
        'utilitybelt>=0.2.1',
        'requests>=2.4.3',
        'pybitcointools==1.1.15',
        'python-bitcoinrpc==0.1',
        'pybitcoin==0.8.2'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
