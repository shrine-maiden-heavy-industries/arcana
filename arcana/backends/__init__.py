# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod

__doc__ = '''\
Arcana backend subsystem.

This module provides the available build backends for arcana.

Currently the following backends are planned:

* Ninja


'''

__all__ = (
	'AbstractBackend',
)

class AbstractBackend(metaclass = ABCMeta):
	'''Backend base class.

	This is the abstract base class that is used
	to implement various backends for Arcana.

	'''

	@property
	@abstractmethod
	def name(self) -> str:
		raise NotImplementedError()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('backends must implement this method')
