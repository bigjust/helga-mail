from setuptools import setup, find_packages

version = '1.0.2'

setup(
    name="helga-mail",
    version=version,
    description=('mail for irc'),
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='irc bot mail',
    author='Justin Caratzas',
    author_email='bigjust@lambdaphil.es',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga_mail'],
    zip_safe=True,
    entry_points = dict(
        helga_plugins = [
            'mail = helga_mail:mail',
        ],
    ),
)
