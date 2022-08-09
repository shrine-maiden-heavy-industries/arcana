# SPDX-License-Identifier: BSD-3-Clause

from importlib import resources
import json


__doc__ = '''\


'''

__all__ = (

	'TOOLCHAINS',

	'get_builtin_toolchain',
)

TOOLCHAINS = (

)


def get_builtin_toolchain(toolchain_name : str) -> dict:
	'''Get bundled toolchain definition

	Parameters
	----------
	toolchain_name : str
		The name of the toolchain definition to get.

	Raises
	------
	ValueError
		If the toolchain definition is not found.

	Returns
	-------
	dict
		The contents of the toolchain definition as a python dict.

	'''

	if toolchain_name not in TOOLCHAINS:
		raise ValueError(f'Unknown Toolchain: {toolchain_name}')
	else:
		return json.loads(resources.read_text('arcana.toolchains.defs', f'{toolchain_name}.json'))
