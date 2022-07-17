# SPDX-License-Identifier: BSD-3-Clause
import logging    as log
from argparse     import ArgumentParser, ArgumentDefaultsHelpFormatter

from rich         import traceback
from rich.logging import RichHandler

from ..           import config

__all__ = (
	'cli_main',
)

def setup_logging(args = None) -> None:
	'''Initialize logging subscriber

	Set up the built-in rich based logging subscriber, and force it
	to be the one at runtime in case there is already one set up.

	Parameters
	----------
	args : argsparse.Namespace
		Any command line arguments passed.

	'''

	level = log.INFO
	if args is not None and args.verbose:
		level = log.DEBUG

	log.basicConfig(
		force    = True,
		format   = '%(message)s',
		datefmt  = '[%X]',
		level    = level,
		handlers = [
			RichHandler(rich_tracebacks = True)
		]
	)

def init_dirs() -> None:
	'''Initialize Arcana application directories.

	Creates all of the appropriate directories that Arcana
	expects, such as the config, and cache directories.

	This uses the XDG_* environment variables if they exist,
	otherwise they assume that all the needed dirs are in the
	running users home directory.

	'''

	dirs = (
		config.ARCANA_CACHE,
		config.ARCANA_DATA,
		config.ARCANA_CONFIG,
	)

	for d in dirs:
		if not d.exists():
			d.mkdir(parents = True, exist_ok = True)

def common_options(parser) -> None:
	'''Initialize common CLI options.

	Registers common options.

	Parameters
	----------
	parser : argparse.ArgumentParser
		The argument parser to register commands with.

	'''

	core_options = parser.add_argument_group('Core configuration options')

	core_options.add_argument(
		'--verbose',
		action = 'store_true',
		help   = 'Enable verbose output during synth and pnr'
	)


def cli_main() -> int:
	try:
		traceback.install()

		init_dirs()
		setup_logging()

		parser = ArgumentParser(
			formatter_class = ArgumentDefaultsHelpFormatter,
			description     = 'Arcana build tool',
			prog            = 'arcana'
		)

		common_options(parser)

		args = parser.parse_args()

		setup_logging(args)

	except KeyboardInterrupt:
		log.info('Bye!')

	return 0
