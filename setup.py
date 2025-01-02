import os
import sys

from setuptools import find_packages
from setuptools import setup

version = '2.9.0'

install_requires = [
    'python-digitalocean>=1.11',
    'setuptools>=41.6.0',
]

if os.environ.get('SNAP_BUILD'):
    install_requires.append('packaging')
else:
    install_requires.extend([
        # We specify the minimum acme and certbot version as the current plugin
        # version for simplicity. See
        # https://github.com/certbot/certbot/issues/8761 for more info.
        f'acme>={version}',
        f'certbot>={version}',
    ])

setup(
    name='certbot-dns-do-jmp',
    version=version,
    description="DNS Jump Domain Digitalocean DNS Authenticator plugin for Certbot",
    url='https://github.com/v-odoo-testing/certbot_dns_do_vct',
    author="Danny Goossen",
    author_email='danny@v-consulting.biz',
    license='MIT',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'certbot.plugins': [
            'dns-do-jmp = certbot_dns_do_jmp.dns_do_jmp:Authenticator',
        ],
    },
)
