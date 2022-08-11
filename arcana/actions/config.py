# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'ConfigAction',
)

class ConfigAction(ArcanaAction):
	pretty_name = 'config'
	short_help  = 'List and change project configuration values'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
