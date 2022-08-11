# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'SetupAction',
)

class SetupAction(ArcanaAction):
	pretty_name = 'setup'
	short_help  = 'Creates a cache file for all other actions to use'
	help        = ''
	description = short_help


	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
