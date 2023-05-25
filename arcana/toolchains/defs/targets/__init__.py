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
	'aarch64-none-elf',
	'aarch64-unknown-elf',
	'aarch64-unknown-linux',
	'alpha-linux-gnu',
	'arm-none-eabi',
	'arm-unknown-linux',
	'avr',
	'frv-none-elf',
	'frv-unknown-elf',
	'frv-unknown-linux',
	'hppa1.1-hp-hpux10',
	'hppa1.1-hp-hpux11',
	'hppa2.0-hp-hpux10',
	'hppa2.0-hp-hpux11',
	'hppa64-none-elf',
	'hppa64-unknown-elf',
	'hppa-none-elf',
	'hppa-unknown-elf',
	'ia64-none-elf',
	'ia64-unknown-elf',
	'ia64-unknown-linux',
	'lm32-none-elf',
	'lm32-unknown-elf',
	'm68k-none-elf',
	'm68k-unknown-elf',
	'm68k-unknown-linux',
	'microblaze-none-elf',
	'microblaze-unknown-elf',
	'microblaze-unknown-linux',
	'mips64-none-elf',
	'mips64-unknown-elf',
	'mips64-unknown-linux',
	'mips-none-elf',
	'mips-unknown-elf',
	'mips-unknown-linux',
	'or1k-none-elf',
	'or1k-unknown-elf',
	'or1k-unknown-linux',
	'ppc64le-none-eabi',
	'ppc64le-none-elf',
	'ppc64le-unknown-elf',
	'ppc64le-unknown-linux',
	'ppc64-none-eabi',
	'ppc64-none-elf',
	'ppc64-unknown-elf',
	'ppc64-unknown-linux',
	'ppcle-none-eabi',
	'ppcle-none-elf',
	'ppcle-unknown-elf',
	'ppcle-unknown-linux',
	'ppc-none-eabi',
	'ppc-none-elf',
	'ppc-unknown-elf',
	'ppc-unknown-linux',
	'riscv32-none-elf',
	'riscv32-unknown-elf',
	'riscv32-unknown-linux',
	'riscv64-none-elf',
	'riscv64-unknown-elf',
	'riscv64-unknown-linux',
	'rx-none-elf',
	'rx-unknown-elf',
	'rx-unknown-linux',
	's390-unknown-linux',
	's390x-ibm-tpf',
	's390x-unknown-linux',
	'sh4-none-elf',
	'sh4-unknown-elf',
	'sh4-unknown-linux',
	'sparc64-none-elf',
	'sparc64-unknown-elf',
	'sparc64-unknown-linux',
	'sparc-none-elf',
	'sparc-unknown-elf',
	'sparc-unknown-linux',
	'vax-linux-gnu',
	'x86_64-none-elf',
	'x86_64-unknown-elf',
	'x86_64-unknown-linux',
	'xtensa-esp32-elf',
	'xtensa-lx106-elf',
	'xtensa-none-elf',
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
		return json.loads(resources.read_text('arcana.toolchains.defs.targets', f'{toolchain_name}.json'))
