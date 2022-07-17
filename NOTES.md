# Arcana Design Notes

## Core Features

* Built-in VCS-aware project *AND* dependency versioning

## File Naming Convention

* `build.arcana` - Build system definition files
* `options.arcana` - Build custom options / configuration (OPTIONAL: Can be defined in the root `build.arcana`)
* `.cache.arcana` - Build configuration cache (automatically added to VCS ignore if one exists)
* `<TARGET>.json` - Arcana target definitions

## Arcana Actions

* `arcana setup [DIR (defaults to build)] [...options]` - Creates a cache file for all other actions to use
* `arcana build [DIR (defaults to cache value)]` - Invoke backend build tool build
* `arcana clean [DIR (defaults to cache value)]` - Invoke backend build tool clean
* `arcana install [DIR (defaults to cache value)] [...options]` - Installed build artifacts (elevates with polkit)
* `arcana dist [DIR (defaults to cache value)] [PKG-Target (one of rpm,deb,pkgbuild,appimage,apk,msi)]` - Create source distribution or Linux package
* `arcana config [DIR (defaults to cache value)] [...options]` - List and change configuration values
* `arcana test [DIR (defaults to cache value)] [...options]` - Run registered tests
* `arcana bench [DIR (defaults to cache value)] [...options]` - Run registered benchmarks
* `arcana debug [DIR (defaults to cache value)] [..options] <TARGET> [...target-options]` - Run specified target in debugger
* `arcana run [DIR (defaults to cache value)] <TARGET> [...target-options]` - Run the given target with specified arguments
* `arcana deps [...options]` - Add/manage dependencies (Support Meson's wrap)
* `arcana lint [...options]` - Lint arcana build files
* `arcana doc [...options]` - Build documentation for project if configured

## Build directory layout

* Mirrored layout
* Internal cached state `<BUILD>/.arcana`
* Logs `<BUILD>/arcana.logs/<TIMESTAMP>-<TOOL>-<TARGET>.log`
* Target Specific build `<BUILD>/<TARGET>/*`
* Symlink installed executables to `<BUILD>/arcana.sysroot/<TARGET>/bin`
* Symlink installed libraries to `<BUILD>/arcana.sysroot/<TARGET>/lib`
* Symlink non-installed executables to `<BUILD>/arcana.sysroot/<TARGET>/contrib`
* Symlink installed include files to `<BUILD>/arcana.sysroot/<TARGET>/include`
* Symlink installed data files to `<BUILD>/arcana.sysroot/<TARGET>/share`
* Documentation output `<BUILD>/docs`

## Default "Magic" Directories

* Project option: `special_dir_prefix: [str|none]`

* Project targets directory - `<ROOT>/<SDIR_PREFIX>/targets`
* Project deps directory - `<ROOT>/<SDIR_PREFIX>/deps`
* Project extensions directory - `<ROOT>/<SDIR_PREFIX>/extensions`
* Project docs directory - `<ROOT>/docs`

## Language Stuff

* `install_with: <TARGET|[...TARGETS]>`

## Target files auto-variables

* `PATH_SEP` - Platform path separator
* `COMPILER_VERSION` - version string for the compiler such as '11.2.0'
* Variable arrays automatically expand and merge
