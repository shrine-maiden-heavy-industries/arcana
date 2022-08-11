# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'DocAction',
)

class DocAction(ArcanaAction):
	pretty_name = 'doc'
	short_help  = 'Build documentation for project if configured'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
