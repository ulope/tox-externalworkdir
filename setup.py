from setuptools import setup

if __name__ == "__main__":
    setup(
        name='tox-externalworkdir',
        version='0.1.0',
        author='Ulrich Petri',
        author_email='mail@ulo.pe',
        description="tox plugin to force tox' workdir outside of the project directory",
        license="MIT license",
        url='http://github.com/ulope/tox-externalworkdir/',
        py_modules=['tox_externalworkdir'],
        entry_points={'tox': ['externalworkdir = tox_externalworkdir']},
        install_requires=['tox>=2.0'],
        zip_safe=False,
        keywords='tox plugin workdir external',
        classifiers=[
            'Operating System :: OS Independent',
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Software Development :: Testing'
        ]
    )
