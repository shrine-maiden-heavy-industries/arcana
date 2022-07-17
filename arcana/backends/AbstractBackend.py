# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = (
	'AbstractBackend'
)

class AbstractBackend(metaclass = ABCMeta):
	'''Backend base class.

	This is the abstract base class that is used
	to implement various backends for Arcana.

	'''
	name = abstractproperty()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('backends must implement this method')
