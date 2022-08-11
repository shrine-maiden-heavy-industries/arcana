# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'CleanAction',
)

class CleanAction(ArcanaAction):
	pretty_name = 'clean'
	short_help  = 'Invoke backend clean'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
