#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup, find_packages
from pathlib    import Path

REPO_ROOT   = Path(__file__).parent
README_FILE = (REPO_ROOT / 'README.md')

def vcs_ver():
	def scheme(version):
		if version.tag and not version.distance:
			return version.format_with('')
		else:
			return version.format_choice('+{node}', '+{node}.dirty')
	return {
		'relative_to': __file__,
		'version_scheme': 'guess-next-dev',
		'local_scheme': scheme
	}

setup(
	name             = 'Arcana',
	use_scm_version  = vcs_ver(),
	author           = 'Aki \'lethalbit\' Van Ness',
	author_email     = 'nya@catgirl.link',
	description      = 'Advanced multi-platform build system',
	license          = 'BSD-3-Clause',
	python_requires  = '~=3.9',
	zip_safe         = True,
	url              = 'https://arcana.shmdn.link/',

	long_description = README_FILE.read_text(),
	long_description_content_type = 'text/markdown',

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
		'requests',
		'Jinja2',
		'arrow',
		'rich>=13.0.0',
	],

	packages         = find_packages(
		where = '.',
		exclude = (
			'tests',
			'tests.*',
			'contrib',
			'contrib.*'
		)
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

		],
		'arcana.toolchains.defs': [
			'components.json',
		],
		'arcana.toolchains.defs.targets': [
			'aarch64-none-elf.json',
			'aarch64-unknown-elf.json',
			'aarch64-unknown-linux.json',
			'alpha-linux-gnu.json',
			'arm-none-eabi.json',
			'arm-unknown-linux.json',
			'avr.json',
			'frv-none-elf.json',
			'frv-unknown-elf.json',
			'frv-unknown-linux.json',
			'hppa1.1-hp-hpux10.json',
			'hppa1.1-hp-hpux11.json',
			'hppa2.0-hp-hpux10.json',
			'hppa2.0-hp-hpux11.json',
			'hppa64-none-elf.json',
			'hppa64-unknown-elf.json',
			'hppa-none-elf.json',
			'hppa-unknown-elf.json',
			'ia64-none-elf.json',
			'ia64-unknown-elf.json',
			'ia64-unknown-linux.json',
			'lm32-none-elf.json',
			'lm32-unknown-elf.json',
			'm68k-none-elf.json',
			'm68k-unknown-elf.json',
			'm68k-unknown-linux.json',
			'microblaze-none-elf.json',
			'microblaze-unknown-elf.json',
			'microblaze-unknown-linux.json',
			'mips64-none-elf.json',
			'mips64-unknown-elf.json',
			'mips64-unknown-linux.json',
			'mips-none-elf.json',
			'mips-unknown-elf.json',
			'mips-unknown-linux.json',
			'or1k-none-elf.json',
			'or1k-unknown-elf.json',
			'or1k-unknown-linux.json',
			'ppc64le-none-eabi.json',
			'ppc64le-none-elf.json',
			'ppc64le-unknown-elf.json',
			'ppc64le-unknown-linux.json',
			'ppc64-none-eabi.json',
			'ppc64-none-elf.json',
			'ppc64-unknown-elf.json',
			'ppc64-unknown-linux.json',
			'ppcle-none-eabi.json',
			'ppcle-none-elf.json',
			'ppcle-unknown-elf.json',
			'ppcle-unknown-linux.json',
			'ppc-none-eabi.json',
			'ppc-none-elf.json',
			'ppc-unknown-elf.json',
			'ppc-unknown-linux.json',
			'riscv32-none-elf.json',
			'riscv32-unknown-elf.json',
			'riscv32-unknown-linux.json',
			'riscv64-none-elf.json',
			'riscv64-unknown-elf.json',
			'riscv64-unknown-linux.json',
			'rx-none-elf.json',
			'rx-unknown-elf.json',
			'rx-unknown-linux.json',
			's390-unknown-linux.json',
			's390x-ibm-tpf.json',
			's390x-unknown-linux.json',
			'sh4-none-elf.json',
			'sh4-unknown-elf.json',
			'sh4-unknown-linux.json',
			'sparc64-none-elf.json',
			'sparc64-unknown-elf.json',
			'sparc64-unknown-linux.json',
			'sparc-none-elf.json',
			'sparc-unknown-elf.json',
			'sparc-unknown-linux.json',
			'vax-linux-gnu.json',
			'x86_64-none-elf.json',
			'x86_64-unknown-elf.json',
			'x86_64-unknown-linux.json',
			'xtensa-esp32-elf.json',
			'xtensa-lx106-elf.json',
			'xtensa-none-elf.json',
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
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',

		'Topic :: Software Development :: Build Tools',

	],

	project_urls     = {
		'Documentation': 'https://arcana.shmdn.link/',
		'Source Code'  : 'https://github.com/shrine-maiden-heavy-industries/arcana',
		'Bug Tracker'  : 'https://github.com/shrine-maiden-heavy-industries/arcana/issues',
	}
)
