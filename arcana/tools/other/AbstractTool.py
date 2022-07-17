# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = (
	'AbstractTool'
)

class AbstractTool(metaclass = ABCMeta):
	'''Tool base class.

	This is the abstract base class that is used
	to implement various tools for Arcana.

	'''
	name = abstractproperty()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('Tools must implement this method')

	@abstractmethod
	def run(self, args):
		'''Tool run

		Raises
		------
		NotImplementedError
			The abstract method must be implemented by the tool

		'''

		raise NotImplementedError('Tools must implement this method')
