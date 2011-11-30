from setuptools import setup, find_packages
import os

version = '1.1dev'
maintainer = 'Timon Tschanz'

setup(name='collective.js.jqtooltip',
      version=version,
      description='This package allows you to use jquery.tooltip in plone.',
      long_description=open('README.txt').read() + '\n' + \
          open(os.path.join('docs', 'History.txt')).read(),

      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.0',
        'Framework :: Plone :: 4.1',
        'Programming Language :: Python'
        ],

      keywords='',
      author='Timon Tschanz',
      author_email='t.tschanz@4teamwork.ch',
      url='https://github.com/collective/collective.js.jqtooltip',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        ],

      entry_points='''
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      ''',
      )
