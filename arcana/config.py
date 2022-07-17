# SPDX-License-Identifier: BSD-3-Clause

from pathlib import Path
from os      import environ

PKG_NAME = 'arcana'

# XDG directories
XDG_HOME        = Path.home()                     if 'XDG_HOME'        not in environ else Path(environ['XDG_HOME'])
XDG_CACHE_DIR   = (XDG_HOME / '.cache')           if 'XDG_CACHE_HOME'  not in environ else Path(environ['XDG_CACHE_HOME'])
XDG_DATA_HOME   = (XDG_HOME / '.local' / 'share') if 'XDG_DATA_HOME'   not in environ else Path(environ['XDG_DATA_HOME'])
XDG_CONFIG_HOME = (XDG_HOME / '.config')          if 'XDG_CONFIG_HOME' not in environ else Path(environ['XDG_CONFIG_HOME'])

# Arcana-specific sub dirs
ARCANA_CACHE   = (XDG_CACHE_DIR   / PKG_NAME)
ARCANA_DATA    = (XDG_DATA_HOME   / PKG_NAME)
ARCANA_CONFIG  = (XDG_CONFIG_HOME / PKG_NAME)
