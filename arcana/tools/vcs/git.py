# SPDX-License-Identifier: BSD-3-Clause

import logging as log
from functools import cached_property
from pathlib   import Path
from typing    import Optional

from .         import AbstractVCS

__all__ = (
	'Git',
)

class Git(AbstractVCS):
	name = 'git'

	@cached_property
	def exec(self) -> Path:
		return self._require_tool('git')

	def __init__(self, repo_path: Path, remote: Optional[str] = None):
		super().__init__(repo_path, remote)


	def supported_platform(self, platform):
		raise NotImplementedError('Tools must implement this method')


	def clone(
		self, *, recursive: bool = False,
		sparse: bool = False, ref: Optional[str] = None
	):
		log.info(f'Cloning into \'{self.repo_path}\'')

		raise NotImplementedError()

	def update(self):
		raise NotImplementedError()

	def describe(self) -> str:
		raise NotImplementedError()

	def remote(self, name: str) -> str:
		raise NotImplementedError()

	def remotes(self) -> list[tuple[str, str]]:
		raise NotImplementedError()

	def is_outdated(self) -> bool:
		raise NotImplementedError()

	def switch(self, ref: str):
		raise NotImplementedError()
