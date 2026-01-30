# Bash completion for ro-start

_ro_start_completions()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="--help --version --no-startup --locale --debug"

    case "${prev}" in
        --locale)
            local locales="en_US tr_TR de es fr it ja ru zh"
            COMPREPLY=( $(compgen -W "${locales}" -- ${cur}) )
            return 0
            ;;
        *)
            ;;
    esac

    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

complete -F _ro_start_completions ro-start
