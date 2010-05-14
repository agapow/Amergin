from setuptools import setup, find_packages
import os

from relais.amergin import __version__

setup(name='relais.amergin',
	version=__VERSION__,
	description="A Django application for curating a Relais repository.",
	long_description=open("README.txt").read() + "\n" +
	  open(os.path.join("docs", "HISTORY.txt")).read(),
	# Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
	  "Programming Language :: Python",
	  "Topic :: Software Development :: Libraries :: Python Modules",
	],
	keywords='science django web epi-informatics',
	author='Paul-Michael Agapow',
	author_email='agapow@bbsrc.ac.uk',
	url='',
	license='BSD',
	packages=find_packages(exclude=['ez_setup']),
	namespace_packages=['relais'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'setuptools',
		# -*- Extra requirements: -*-
	],
	entry_points="""
		# -*- Entry points: -*-
	""",
)
