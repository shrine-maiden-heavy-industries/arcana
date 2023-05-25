# SPDX-License-Identifier: BSD-3-Clause

from abc     import abstractmethod
from pathlib import Path
from typing  import Optional

from ..      import AbstractTool

__doc__ = '''\

Arcana Tools: VCS

'''

__all__ = (
	'AbstractVCS',
)

class AbstractVCS(AbstractTool):
	'''VCS base class.

	This is the abstract base class that is used
	to implement various version control systems
	for Arcana.

	'''

	def __init__(self, repo_path: Path, remote: Optional[str] = None):
		self.repo_path = repo_path
		self.remote    = remote

	@abstractmethod
	def clone(
		self, *, recursive: bool = False,
		sparse: bool = False, ref: Optional[str] = None
	):
		'''
		Clone the given repository if not already.

		Parameters
		----------
		recursive : bool
			On supported VCS', recursively clone the repository and initialize submodules.

		sparse : bool
			On supported VCS', do a sparse clone of the repository.

		ref : Optional[str]
			On supported VCS', check out the given ref-spec/tag/branch after clone.

		'''
		raise NotImplementedError()

	@abstractmethod
	def update(self):
		''' Update the repository '''

		raise NotImplementedError()

	@abstractmethod
	def describe(self) -> str:
		''' Return '''
		raise NotImplementedError()

	@abstractmethod
	def remote(self, name: str) -> Optional[str]:
		'''
		Get the remote uri by name.

		Parameters
		----------
		name : str
			The name of the remote to get

		Returns
		-------
		Optional[str]
			The URL for the named remote or None if not found.

		'''
		raise NotImplementedError()

	@abstractmethod
	def remotes(self) -> list[tuple[str, str]]:
		'''
		Get all remotes from the repository.

		Returns
		-------
		list[tuple[str, str]]
			A list of name, url pairs describing each remote.

		'''

		raise NotImplementedError()

	@abstractmethod
	def is_outdated(self) -> bool:
		'''
		Check if the local copy of the remote is out of date compared
		to the default remote.

		'''

		raise NotImplementedError()

	@abstractmethod
	def switch(self, ref: str):
		'''
		Switch from the current active ref/branch/tag to the given one.

		Parameters
		----------
		ref : str
			The ref-spec to switch to/checkout.

		'''

		raise NotImplementedError()
