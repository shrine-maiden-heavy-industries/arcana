# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'BenchmarkAction',
)

class BenchmarkAction(ArcanaAction):
	pretty_name = 'bench'
	short_help  = 'Run registered benchmarks'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
