# SPDX-License-Identifier: BSD-3-Clause

import json
from pathlib import Path

from .defs import ALL_TARGETS, get_builtin_target


__doc__ = '''\

Arcana target subsystem.

This module implements the machinery for managing and parsing architecture targets
for Arcana.

As Arcana natively supports large heterogeneous architecture projects, this module
provides a collection of built-in target definitions, as well as targets for the
build machine, and all the needed machinery to define other possible targets.

'''

__all__ = (
	'Target',
)


class Target:
	'''Machine target definition'''


	def __init__(self):
		pass


	@staticmethod
	def from_host():
		'''Get build machines target definition'''

		pass

	@staticmethod
	def from_file(target_file : Path):
		'''Get target object from target definition file'''


		pass

	@staticmethod
	def from_definition(target_def : dict):
		'''Get target object from given target definition dict'''

		pass


	@staticmethod
	def from_builtin(target_name : str):
		'''Get Target object from built-in target definition'''
		pass

	@staticmethod
	def builtin_targets():
		''' Get a list of all built-in target definitions'''

		return ALL_TARGETS
