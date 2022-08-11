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
	'aarch64-none-elf.json',
	'aarch64-unknown-elf.json',
	'aarch64-unknown-linux.json',
	'alpha-linux-gnu.json',
	'arm-none-eabi.json',
	'arm-unknown-linux.json',
	'avr.json',
	'frv-none-elf.json',
	'frv-unknown-elf.json',
	'frv-unknown-linux.json',
	'hppa1.1-hp-hpux10.json',
	'hppa1.1-hp-hpux11.json',
	'hppa2.0-hp-hpux10.json',
	'hppa2.0-hp-hpux11.json',
	'hppa64-none-elf.json',
	'hppa64-unknown-elf.json',
	'hppa-none-elf.json',
	'hppa-unknown-elf.json',
	'ia64-none-elf.json',
	'ia64-unknown-elf.json',
	'ia64-unknown-linux.json',
	'lm32-none-elf.json',
	'lm32-unknown-elf.json',
	'm68k-none-elf.json',
	'm68k-unknown-elf.json',
	'm68k-unknown-linux.json',
	'microblaze-none-elf.json',
	'microblaze-unknown-elf.json',
	'microblaze-unknown-linux.json',
	'mips64-none-elf.json',
	'mips64-unknown-elf.json',
	'mips64-unknown-linux.json',
	'mips-none-elf.json',
	'mips-unknown-elf.json',
	'mips-unknown-linux.json',
	'or1k-none-elf.json',
	'or1k-unknown-elf.json',
	'or1k-unknown-linux.json',
	'ppc64le-none-eabi.json',
	'ppc64le-none-elf.json',
	'ppc64le-unknown-elf.json',
	'ppc64le-unknown-linux.json',
	'ppc64-none-eabi.json',
	'ppc64-none-elf.json',
	'ppc64-unknown-elf.json',
	'ppc64-unknown-linux.json',
	'ppcle-none-eabi.json',
	'ppcle-none-elf.json',
	'ppcle-unknown-elf.json',
	'ppcle-unknown-linux.json',
	'ppc-none-eabi.json',
	'ppc-none-elf.json',
	'ppc-unknown-elf.json',
	'ppc-unknown-linux.json',
	'riscv32-none-elf.json',
	'riscv32-unknown-elf.json',
	'riscv32-unknown-linux.json',
	'riscv64-none-elf.json',
	'riscv64-unknown-elf.json',
	'riscv64-unknown-linux.json',
	'rx-none-elf.json',
	'rx-unknown-elf.json',
	'rx-unknown-linux.json',
	's390-unknown-linux.json',
	's390x-ibm-tpf.json',
	's390x-unknown-linux.json',
	'sh4-none-elf.json',
	'sh4-unknown-elf.json',
	'sh4-unknown-linux.json',
	'sparc64-none-elf.json',
	'sparc64-unknown-elf.json',
	'sparc64-unknown-linux.json',
	'sparc-none-elf.json',
	'sparc-unknown-elf.json',
	'sparc-unknown-linux.json',
	'vax-linux-gnu.json',
	'x86_64-none-elf.json',
	'x86_64-unknown-elf.json',
	'x86_64-unknown-linux.json',
	'xtensa-esp32-elf.json',
	'xtensa-lx106-elf.json',
	'xtensa-none-elf.json',
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
