#compdef arcana "python -m arcana"
# ln -sv arcana.zsh _arcana
# unfunction _arcana && autoload -U _arcana
# SPDX-License-Identifier: BSD-3-Clause


_arcana_command() {
	local -a commands=(
		'setup[Setup arcana build envrionment]'
		'build[Invoke backend build tool]'
		'clean[Clean build directory]'
		'install[Install build artifacts]'
		'dist[Create source distribution artifacts]'
		'config[List and change build configuration values]'
		'test[Run registered tests]'
		'bench[Run registered benchmarks]'
		'debug[Invoke target in debugger]'
		'run[Invoke target]'
		'deps[Add and manage dependencies]'
		'lint[Lint arcana build files]'
		'doc[Build project documentation]'
	)
	_values 'arcana commands' : $commands
}


_arcana_setup() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_build() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_clean() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_install() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_dist() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_config() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_test() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_setup() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_bench() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_debug() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_run() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_deps() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_lint() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}

_arcana_doc() {
	local arguments
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[Show help and exit]'
	)

	_arguments -s : $arguments && return

	return $ret
}


_arcana() {
	local arguments context curcontext=$curcontext state state_descr line
	integer ret=1

	arguments=(
		'(-h --help)'{-h,--help}'[show version and help then exit]'
		'--verbose[verbose logging]'
		'(-): :->command'
		'(-)*:: :->arguments'
	)

	_arguments -s -C : $arguments && return

	case $state in
		(command)
			_arcana_command && ret=0
			;;
		(arguments)
			curcontext=${curcontext%:*:*}:arcana-$words[1]:
			case $words[1] in
				(setup)
					_arcana_setup && ret=0
					;;
				(build)
					_arcana_build && ret=0
					;;
				(clean)
					_arcana_clean && ret=0
					;;
				(install)
					_arcana_install && ret=0
					;;
				(config)
					_arcana_config && ret=0
					;;
				(test)
					_arcana_test && ret=0
					;;
				(bench)
					_arcana_bench && ret=0
					;;
				(debug)
					_arcana_debug && ret=0
					;;
				(run)
					_arcana_run && ret=0
					;;
				(deps)
					_arcana_deps && ret=0
					;;
				(lint)
					_arcana_lint && ret=0
					;;
				(doc)
					_arcana_doc && ret=0
					;;
			esac
			;;
	esac

	return $ret
}

_arcana
