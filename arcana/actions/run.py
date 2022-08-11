# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'RunAction',
)

class RunAction(ArcanaAction):
	pretty_name = 'run'
	short_help  = 'Run the given target with specified arguments'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
