# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'BuildAction',
)

class BuildAction(ArcanaAction):
	pretty_name = 'build'
	short_help  = 'Invoke backend build tool'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
