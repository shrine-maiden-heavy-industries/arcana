# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'TestAction',
)

class TestAction(ArcanaAction):
	pretty_name = 'test'
	short_help  = 'Run registered tests'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
