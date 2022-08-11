# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'DistAction',
)

class DistAction(ArcanaAction):
	pretty_name = 'dist'
	short_help  = 'Create source distribution and/or Linux package'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
