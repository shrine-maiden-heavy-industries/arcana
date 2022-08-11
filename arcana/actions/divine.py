# SPDX-License-Identifier: BSD-3-Clause

from . import ArcanaAction

__doc__ = '''\

'''

__all__ = (
	'DivineAction',
)

class DivineAction(ArcanaAction):
	pretty_name = 'divine'
	short_help  = 'Migrate a Meson/CMake/Autotools project to arcana'
	help        = ''
	description = short_help

	def __init__(self):
		super().__init__()

	def register_args(self, parser):
		pass

	def run(self, args):
		pass
