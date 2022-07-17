#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
import sys
from pathlib import Path

try:
	from arcana.main import cli_main
except ImportError:
	arcana_path = Path(sys.argv[0]).resolve()

	if (arcana_path.parent / 'arcana').is_dir():
		sys.path.insert(0, str(arcana_path.parent))

	from arcana.main import cli_main

sys.exit(cli_main())
