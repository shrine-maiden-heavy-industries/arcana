# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = (
	'AbstractCompiler'
)

class AbstractCompiler(metaclass = ABCMeta):
	'''Compiler base class.

	This is the abstract base class that is used
	to implement various compilers for Arcana.

	'''
	name = abstractproperty()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('Compilers must implement this method')
