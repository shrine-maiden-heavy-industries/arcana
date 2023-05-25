# SPDX-License-Identifier: BSD-3-Clause

import argparse
import logging                 as log
import json
from multiprocessing           import cpu_count

from rich                      import print
from rich.tree                 import Tree

from .                         import ArcanaAction
from ..config                  import (
	ARCANA_USER_TOOLCHAINS,
	ARCANA_TOOLCHAIN_INDEX,
	XDG_BIN_HOME
)

from ..toolchains.defs.targets import (
	TOOLCHAINS,
	get_builtin_toolchain
)

__doc__ = '''\

'''

__all__ = (
	'ToolchainAction',
)

class ToolchainAction(ArcanaAction):
	pretty_name = 'toolchain'
	short_help  = 'Arcana toolchain management'
	help        = 'Install, Update, Remove, and Build cross-compiler toolchains'
	description = short_help

	def _list(self, args: argparse.Namespace) -> int:
		toolchain_tree = Tree(
			'[bright_cyan]Arcana Toolchains[/]',
			guide_style = 'blue'
		)

		if args.list_installed:
			if len(self.toolchain_index['toolchains']) > 0:
				toolchain_tree.label = f'{toolchain_tree.label} - [green]Installed[/]'
				for toolchain in self.toolchain_index['toolchains']:
					toolchain_tree.add(f"{toolchain['triple']}")
			else:
				log.warn('There are no currently installed toolchains')
				return 0
		else:
			for toolchain in TOOLCHAINS:
				tc = get_builtin_toolchain(toolchain)
				if not tc['enabled']:
					continue

				tc_node = toolchain_tree.add(f'[magenta]{toolchain}[/]')
				if args.list_detailed:
					for k, v in tc['properties'].items():
						tc_node.add(f'[cyan]{k}[/]: [green]{v}[/]')
					tc_components = tc_node.add('[yellow]Components[/]')
					for k, v in tc['components'].items():
						if k == 'libc':
							tc_components.add(f'[bright_blue]{k}[/] ([bright_yellow]{v["libc"]}[/])')
						else:
							tc_components.add(f'[bright_blue]{k}[/]')

		print(toolchain_tree)
		return 0

	def _build(self, args: argparse.Namespace) -> int:
		return 0

	def _rm(self, args: argparse.Namespace) -> int:
		if len(self.toolchain_index['toolchains']) == 0:
			log.error('No toolchains built and installed, unable to remove anything')
			return 1



		return 0

	def __init__(self):
		super().__init__()

		if not ARCANA_TOOLCHAIN_INDEX.exists():
			self.toolchain_index = {
				"$schema": "https://raw.githubusercontent.com/shrine-maiden-heavy-industries/arcana/main/contrib/schemas/aracana.toolchain-index.schema.json",
				"toolchains": []
			}
			self._save_index()
		else:
			with ARCANA_TOOLCHAIN_INDEX.open('r') as f:
				self.toolchain_index = json.load(f)

		self.subactions = {
			'ls'   : self._list,
			'build': self._build,
			'rm'   : self._rm,
		}

	def _in_index(self, triple: str) -> bool:
		if len(self.toolchain_index['toolchains']) == 0:
			return False



	def _save_index(self) -> None:
		with ARCANA_TOOLCHAIN_INDEX.open('w') as f:
			json.dump(self.toolchain_index, f)

	def register_args(self, parser: argparse.ArgumentParser) -> None:
		subactions = parser.add_subparsers(
			dest = 'sub_action',
			required = True
		)

		list_action = subactions.add_parser(
			'ls',
			help = 'list known and installed toolchains'
		)

		list_action.add_argument(
			'--installed', '-i',
			dest   = 'list_installed',
			action = 'store_true',
			help   = 'List only installed toolchains'
		)

		list_action.add_argument(
			'--detailed', '-d',
			dest   = 'list_detailed',
			action = 'store_true',
			help   = 'Detailed information for toolchain listing'
		)

		build_action = subactions.add_parser(
			'build',
			help = 'build specified toolchain'
		)

		build_action.add_argument(
			'--jobs', '-j',
			dest    = 'build_jobs',
			type    = int,
			default = cpu_count,
			help    = 'Number to parallel jobs to run'
		)

		remove_action = subactions.add_parser(
			'rm',
			help = 'remove installed toolchain'
		)

		remove_action.add_argument(
			'--all', '-a',
			dest   = 'remove_all',
			action = 'store_true',
			help   = 'Remove all built and installed toolchains'
		)



	def run(self, args: argparse.Namespace) -> int:
		return self.subactions.get(args.sub_action, lambda s, a: 1)(args)
