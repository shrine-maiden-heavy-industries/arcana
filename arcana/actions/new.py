# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'NewAction',
)

class NewAction(ArcanaAction):
	pretty_name = 'new'
	short_help  = 'Create a project based on a template in a new directory'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
