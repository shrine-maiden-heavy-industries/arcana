# SPDX-License-Identifier: BSD-3-Clause
import logging      as log
from argparse       import ArgumentParser, ArgumentDefaultsHelpFormatter
from pathlib        import Path

from rich           import traceback
from rich.logging   import RichHandler

from ..             import actions
from ..             import config
from ..core.collect import collect_members, predicate_action

__doc__ = '''\

Arcana main execution entrypoint

This module implements the main CLI interface for Arcana.

'''

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

		config.ARCANA_USER_TARGETS,
		config.ARCANA_USER_EXTENSIONS,
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

		ACTIONS = collect_members(
			Path(actions.__path__[0]),
			predicate_action,
			f'{actions.__name__}.'
		)


		parser = ArgumentParser(
			formatter_class = ArgumentDefaultsHelpFormatter,
			description     = 'Arcana build tool',
			prog            = 'arcana'
		)

		common_options(parser)

		action_parser = parser.add_subparsers(
			dest = 'action',
			required = False
		)

		if len(ACTIONS) > 0:
			for act in ACTIONS:
				action = act['instance']
				p = action_parser.add_parser(
						act['name'],
						help = action.short_help,
					)
				action.register_args(p)

		args = parser.parse_args()

		setup_logging(args)

		if args.action is not None:
			act = list(filter(lambda a: a['name'] == args.action, ACTIONS))[0]
			return act['instance'].run(args)

	except KeyboardInterrupt:
		log.info('Bye!')

	return 0
