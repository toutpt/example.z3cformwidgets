from setuptools import setup, find_packages
import os

version = '1.0dev'

setup(name='example.z3cformwidgets',
      version=version,
      description="This add is a reference guide of existing z3cform widgets",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['example'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.autoform',
          'plone.app.z3cform',
          'plone.formwidget.autocomplete',
          'plone.formwidget.captcha',
          'plone.formwidget.contenttree',
          'plone.formwidget.recaptcha',
          'plone.formwidget.namedfile',
          'collective.z3cform.colorpicker',
          'collective.z3cform.datetimewidget',
          'collective.z3cform.keywordwidget',
          'collective.z3cform.norobots',
          'collective.z3cform.wizard',
          'collective.z3cform.filewidget',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
