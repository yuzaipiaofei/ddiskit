#!/usr/bin/python

from setuptools import setup

setup(
    name="ddiskit",
    version="3.2",
    author="Petr Oros",
    author_email="poros@redhat.com",
    description=("Red Hat tool for create Driver Update Disk"),
    license="GPLv3",
    url="http://git.engineering.redhat.com/git/users/poros/ddiskit.git/",
    packages=['ddiskit'],
    package_dir={'ddiskit': 'src/'},
    data_files=[('/etc/bash_completion.d', ['ddiskit.bash']),
                ('/usr/share/ddiskit/templates',
                    ['templates/spec', 'templates/config']),
                ('/usr/share/ddiskit/profiles', ['profiles/default']),
                ('/usr/share/ddiskit', ['ddiskit.config']),
                ],
    entry_points={
        'console_scripts': [
            'ddiskit=ddiskit.ddiskit:main',
        ],
    },
)
