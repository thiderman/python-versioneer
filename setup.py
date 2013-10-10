from distutils.core import setup


setup(
    name='versioneer',
    version='0.8',  # The cobbler's children have no shoes :>
    url='https://github.com/warner/python-versioneer',
    author='Brian Warner',
    author_email='warner-github@lothar.com',
    description=('version-string management for VCS-controlled trees'),
    license='Public Domain',
    packages=['versioneer', 'versioneer.git'],
    scripts=[
        'bin/install-versioneer'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Public Domain',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Version Control',
    ],
)
