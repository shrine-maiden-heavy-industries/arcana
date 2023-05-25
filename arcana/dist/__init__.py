# SPDX-License-Identifier: BSD-3-Clause

from abc import ABCMeta, abstractmethod


__doc__ = '''\
Arcana packaging / distribution subsystem


This module provides the means to create various packages for distribution on
a various collection of platforms, with an easy to extend API.

The current list of supported and planned distribution methods are as follows:

* tar
* zip
* rpm
* deb
* pkgbuild
* appimage
* apk
* msi


'''

__all__ = (
	'AbstractDistribution',
)

class AbstractDistribution(metaclass = ABCMeta):
	'''Distribution base class.

	This is the abstract base class that is used
	to implement various distribution methods for Arcana.

	'''

	@property
	@abstractmethod
	def name(self) -> str:
		raise NotImplementedError()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('Distributions must implement this method')
