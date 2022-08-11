# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'InstallAction',
)

class InstallAction(ArcanaAction):
	pretty_name = 'install'
	short_help  = 'Install build artifacts'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
