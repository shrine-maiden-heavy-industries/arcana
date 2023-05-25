# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod


__doc__ = '''\

Arcana extension subsystem.

This module provides the build-in extensions for arcana to allow support for various
packages and frameworks, like Qt or Boost.

Currently the following extensions are planned:

* i18n
* pkgconfig
* python
* qt[5,6]


'''

__all__ = (
	'AbstractExtension',
)

class AbstractExtension(metaclass = ABCMeta):
	'''Extension base class.

	This is the abstract base class that is used
	to implement various extension methods for Arcana.

	'''

	@property
	@abstractmethod
	def name(self) -> str:
		raise NotImplementedError()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('Extensions must implement this method')
