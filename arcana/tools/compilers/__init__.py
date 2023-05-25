# SPDX-License-Identifier: BSD-3-Clause

from abc     import abstractmethod

from ..      import AbstractTool
from ...core import Languages

__doc__ = '''\

Arcana Tools: Compilers

'''

__all__ = (

)

class AbstractCompiler(AbstractTool):
	'''Compiler base class.

	This is the abstract base class that is used
	to implement various compilers for Arcana.

	'''

	@property
	@abstractmethod
	def languages(self) -> tuple[Languages]:
		''' Returns a list of supported languages for this compiler '''
		raise NotImplementedError()
