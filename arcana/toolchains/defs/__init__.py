# SPDX-License-Identifier: BSD-3-Clause

from importlib import resources
import json

__doc__ = '''\

'''

__all__ = (
	'get_builtin_toolchain_components',
)

def get_builtin_toolchain_components() -> dict:
	'''Get bundled toolchain component definition

	Returns
	-------
	dict
		The contents of the toolchain definition as a python dict.

	'''
	return json.loads(resources.read_text('arcana.toolchains.defs', 'components.json'))
