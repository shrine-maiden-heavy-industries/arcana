# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = (
	'AbstractExtension'
)

class AbstractExtension(metaclass = ABCMeta):
	'''Extension base class.

	This is the abstract base class that is used
	to implement various extension methods for Arcana.

	'''
	name = abstractproperty()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('Extensions must implement this method')
