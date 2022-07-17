#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup, find_packages

def vcs_ver():
	def scheme(version):
		if version.tag and not version.distance:
			return version.format_with("")
		else:
			return version.format_choice("+{node}", "+{node}.dirty")
	return {
		"relative_to": __file__,
		"version_scheme": "guess-next-dev",
		"local_scheme": scheme
	}

setup(
	name             = 'Arcana',
	use_scm_version  = vcs_ver(),
	author           = 'Aki \'lethalbit\' Van Ness',
	author_email     = 'nya@catgirl.link',
	description      = 'Advanced multi-platform build system',
	long_description = 'TODO',
	license          = 'BSD-3-Clause',
	python_requires  = '~=3.8',
	zip_safe         = True,
	url              = 'https://github.com/shrine-maiden-heavy-industries/arcana',

	setup_requires   = [
		'wheel',
		'setuptools',
		'setuptools_scm'
	],

	extras_require   = {
		'build': [
			'ninja>=1.8.2'
		]
	},

	install_requires = [
		'Jinja2',
		'arrow',
		'rich~=12.2.0',
	],

	packages         = find_packages(
		where = '.'
	),

	entry_points     = {
		'console_scripts': [
			'arcana = arcana.main:cli_main',
		],

	},

	package_data     = {
		'arcana.targets.defs.embedded': [
			'atxmega256a3u.json',
			'tm4c123gh6pm.json',
		],
		'arcana.targets.defs.generic': [

		]
	},

	classifiers      = [
		'Development Status :: 4 - Beta',

		'Environment :: Console',

		'Intended Audience :: Developers',

		'License :: OSI Approved :: BSD License',

		'Natural Language :: English',

		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: AIX',
		'Operating System :: POSIX :: BSD',
		'Operating System :: POSIX :: Linux',
		'Operating System :: POSIX :: SunOS/Solaris',

		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',

		'Topic :: Software Development :: Build Tools',

	],

	project_urls     = {
		'Documentation': 'https://github.com/shrine-maiden-heavy-industries/arcana',
		'Source Code'  : 'https://github.com/shrine-maiden-heavy-industries/arcana',
		'Bug Tracker'  : 'https://github.com/shrine-maiden-heavy-industries/arcana/issues',
	}
)
