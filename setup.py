from setuptools import setup, find_packages
import os

version = '1.1dev'
maintainer = 'Timon Tschanz'

setup(name='collective.js.jqtooltip',
      version=version,
      description="This Package allows you to use jquery.tooltip",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "History.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python"
        ],
      keywords='',
      author='Timon Tschanz',
      author_email='t.tschanz@4teamwork.ch',
      url='http://bassistance.de/jquery-plugins/jquery-plugin-tooltip/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
