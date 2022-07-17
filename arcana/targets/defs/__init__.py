# SPDX-License-Identifier: BSD-3-Clause

from importlib import resources
import json

from .embedded import TARGET_LIST as EMBEDDED_TARGETS
from .generic  import TARGET_LIST as GENERIC_TARGETS

__all__ = (
	'EMBEDDED_TARGETS',
	'GENERIC_TARGETS',
	'ALL_TARGETS',

	'get_builtin_target',
)

ALL_TARGETS = (
	*EMBEDDED_TARGETS,
	*GENERIC_TARGETS
)

def get_builtin_target(target_name : str) -> dict:
	'''Get bundled target definition

	Parameters
	----------
	target_name : str
		The name of the target to get.

	Raises
	------
	ValueError
		If the target definition is not found.

	Returns
	-------
	dict
		The contents of the target definition as a python dict.

	'''

	if target_name not in ALL_TARGETS:
		raise ValueError(f'Unknown Target: {target_name}')

	if target_name in GENERIC_TARGETS:
		return json.loads(resources.read_text('arcana.targets.defs.generic', f'{target_name}.json'))
	elif target_name in EMBEDDED_TARGETS:
		return json.loads(resources.read_text('arcana.targets.defs.embedded', f'{target_name}.json'))
	else:
		raise ValueError(f'Target {target_name} not in generic nor embedded targets, yet in all targets?')
