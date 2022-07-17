# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod, abstractproperty

__all__ = (
	'AbstractDistribution'
)

class AbstractDistribution(metaclass = ABCMeta):
	'''Distribution base class.

	This is the abstract base class that is used
	to implement various distribution methods for Arcana.

	'''
	name = abstractproperty()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('Distributions must implement this method')
