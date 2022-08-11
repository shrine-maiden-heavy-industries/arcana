# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

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

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
