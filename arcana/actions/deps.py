# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'DepsAction',
)

class DepsAction(ArcanaAction):
	pretty_name = 'deps'
	short_help  = 'Add/manage dependencies'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
