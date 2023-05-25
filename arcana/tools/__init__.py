# SPDX-License-Identifier: BSD-3-Clause

import logging  as log
from abc        import ABCMeta, abstractmethod
from functools  import cached_property
from os         import environ
from pathlib    import Path
from shutil     import which
from subprocess import run
from typing     import Optional, Union

__doc__ = '''\

Arcana tool subsystem.

This module provides the infrastructure to detect and wrap needed tools for various
build platforms.


The current categories are as follows:

* compilers - Tools that explicitly translate a higher-level language into machine-code or assembly
* linkers - Tools that combine multiple object files into a single unit.
* other - Any other tools, like objcopy, objdump, strip, gdb, etc.

'''

__all__ = (
	'AbstractTool',
	'ToolNotFound',
)

class ToolNotFound(Exception):
	pass

class AbstractTool(metaclass = ABCMeta):
	'''
	Tool base class.

	This is the abstract base class that is used
	to implement various tools for Arcana.

	'''

	def _tool_env_var(self, name: str) -> str:
		'''
		Convert the given tool name into a normalized version for
		environment variables.

		This generally means replacing any `-`'s with `_`'s and any
		`+`'s with `X`'s and converting the entire name to uppercase.

		Parameters
		----------
		name : str
			The tool/executable name.

		Returns
		-------
		str
			The name of the environment variable used to look for
			for tool overrides.

		'''

		return name.upper().replace('-', '_').replace('+', 'X')

	def _get_tool(self, name: str) -> str:
		'''
		Get the tool name or path if overridden by an environment variable.

		Parameters
		----------
		name : str
			The tool/executable name.

		Returns
		-------
		str
			The tool/executable name if not found in the environment.

		'''

		return environ.get(self._tool_env_var(name), name)

	def _has_tool(self, name: str) -> bool:
		'''
		Check to see if the tool or executable is in the current PATH.

		Parameters
		----------
		name : str
			The tool/executable name.

		Returns
		-------
		bool
			If the tool/executable was found in the current system PATH.

		'''

		return which(self._get_tool(name)) is not None

	def _require_tool(self, name: str) -> Path:
		'''
		Return the fully resolved path to the requested tool or executable
		if found, otherwise throw a ToolNotFound exception.

		Parameters
		----------
		name : str
			The tool/executable name.

		Returns
		-------
		Path
			The fully qualified path to the executable / tool.

		Raises
		------
		ToolNotFound

		'''

		log.debug(f'Searching for tool \'{name}\'...')

		env_var = self._tool_env_var(name)
		path = self._get_tool(name)
		if which(path) is None:
			if env_var in environ:
				raise ToolNotFound(
					f'Could not find required tool {name} in {path} as specified via '
					f'the {env_var} environment variable'
				)
			else:
				raise ToolNotFound(
					f'Could not find required tool {name} in PATH. Place '
					'it directly in PATH or specify path explicitly '
					f'via the {env_var} environment variable'
				)
		return Path(path).resolve()


	@property
	@abstractmethod
	def name(self) -> str:
		raise NotImplementedError()

	@cached_property
	@abstractmethod
	def exec(self) -> Path:
		''' The fully resolved path to the given tool '''

		raise NotImplementedError()

	def __init__(self):
		pass

	@abstractmethod
	def supported_platform(self, platform):
		raise NotImplementedError('Tools must implement this method')


	def _run(
		self, *args: str, input: Optional[str] = None,
		print_output: bool = False, capture: bool = False
	) -> Union[int, tuple[int, str, str]]:
		'''
		Run tool with given arguments.

		Parameters
		----------
		args : tuple[str]
			Arguments to pass to the tool

		input : Optional[str]
			Input to pass to the tool on STDIN

		print_output : bool
			Print collected output from STDOUT (default: False)

		capture : bool
			Return STDOUT and STDERR with the return code (default: False)

		Returns
		-------
		tuple[int, str, str]
			The return code, STDOUT, and STDERR. (if capture is true)

		int
			The return code. (if capture is false)

		'''

		proc = run(
			[ str(self.exec), *args ], input = input
		)

		if print_output and len(proc.stdout) > 0:
			log.log(proc.stdout)

		if len(proc.stderr) > 0:
			log.error(proc.stderr)
		if capture:
			return (proc.returncode, proc.stdout, proc.stderr)
		return proc.returncode
