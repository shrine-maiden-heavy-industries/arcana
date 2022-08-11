# SPDX-License-Identifier: BSD-3-Clause
import logging       as log
from pathlib         import Path
from multiprocessing import cpu_count
from shutil          import rmtree

from ..config        import (
	XDG_BIN_HOME, ARCANA_CACHE, ARCANA_USER_TOOLCHAINS
)

from .defs           import get_builtin_toolchain_components
from .defs.targets   import get_builtin_toolchain, TOOLCHAINS

__doc__ = '''\

'''

__all__ = (

)

TOOLCHAIN_CACHE = (ARCANA_CACHE / 'toolchains')

BUILD_DIR    = (TOOLCHAIN_CACHE / 'build')
SOURCE_DIR   = (TOOLCHAIN_CACHE / 'src')
DOWNLOAD_DIR = (TOOLCHAIN_CACHE / 'download')

def _initialize_dirs():
	if not TOOLCHAIN_CACHE.exists():
		TOOLCHAIN_CACHE.mkdir(parents = True)

	if not BUILD_DIR.exists():
		BUILD_DIR.mkdir()

	if not SOURCE_DIR.exists():
		SOURCE_DIR.mkdir()

	if not DOWNLOAD_DIR.exists():
		DOWNLOAD_DIR.mkdir()

def download_file(url: str, file: str, checksum: str) -> bool:
	from hashlib import sha512
	import requests
	import rich.progress as pb

	file_url = f'{url}/{file}'
	file_dest = (DOWNLOAD_DIR / file)

	if file_dest.exists():
		log.info(f'Already have {file}, skipping')
		return True

	log.info(f'Downloading \'{file}\' from \'{file_url}\'...')

	progress = pb.Progress(
		pb.TextColumn('Downloading [bold blue]{task.fields[filename]}', justify = 'right'),
		pb.BarColumn(),
		'[progress.percentage]{task.percentage:>3.1f}%',
		' ',
		pb.DownloadColumn(),
		' ',
		pb.TransferSpeedColumn(),
		' ',
		pb.TimeRemainingColumn()
	)

	with requests.get(file_url, allow_redirects = True) as r:
		task = progress.add_task('download', filename = file, start = False)
		if not r.ok:
			log.error(f'Unable to download \'{file_url}\', got {r.status_code}')
			return False
		else:
			h = sha512()
			progress.update(task, total = int(r.headers['Content-length']))
			with open(file_dest, 'wb') as f:
				progress.start_task(task)
				for chunk in r.iter_content(chunk_size = 8192):
					f.write(chunk)
					h.update(chunk)
					progress.update(task, advance = len(chunk))

			log.info(f'Downloaded \'{file}\'')
			log.info('Checking digest...')

			if h.hexdigest() != checksum:
				log.error(f'File checksum failed! got: {h.hexdigest()} wanted: {checksum}')
				return False
			return True
