# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'DebugAction',
)

class DebugAction(ArcanaAction):
	pretty_name = 'debug'
	short_help  = 'Run specified target in debugger'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
