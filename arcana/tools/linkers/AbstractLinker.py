# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = (
	'AbstractLinker'
)

class AbstractLinker(metaclass = ABCMeta):
	'''Linker base class.

	This is the abstract base class that is used
	to implement various Linkers for Arcana.

	'''
	name = abstractproperty()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('Linkers must implement this method')
