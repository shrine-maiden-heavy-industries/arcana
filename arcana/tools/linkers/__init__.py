# SPDX-License-Identifier: BSD-3-Clause

from abc import abstractmethod

from ..  import AbstractTool

__doc__ = '''\

Arcana Tools: Linkers

'''

__all__ = (

)

class AbstractLinker(AbstractTool):
	'''Linker base class.

	This is the abstract base class that is used
	to implement various Linkers for Arcana.

	'''
