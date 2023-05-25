# SPDX-License-Identifier: BSD-3-Clause

from enum import Enum, unique, auto

__doc__ = '''\

Arcana core support subsystem.

This module provides various support utilities and objects to make implementing
the rest of Arcana easier.

'''

__all__ = (
	'Languages',
)

@unique
class Languages(Enum):
	CXX = auto()
	C   = auto()
