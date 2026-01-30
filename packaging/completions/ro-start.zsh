#compdef ro-start

_ro_start() {
    local -a opts
    opts=(
        '--help[Show help information]'
        '--version[Show version information]'
        '--no-startup[Do not show at startup]'
        '--locale[Set interface language]:locale:(en_US tr_TR de es fr it ja ru zh)'
        '--debug[Enable debug logging]'
        '-d[Enable debug logging]'
    )

    _arguments -s $opts
}

_ro_start "$@"
