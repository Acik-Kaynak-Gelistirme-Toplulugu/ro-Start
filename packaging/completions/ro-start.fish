# Fish completion for ro-start

complete -c ro-start -l help -d 'Show help information'
complete -c ro-start -l version -d 'Show version information'
complete -c ro-start -l no-startup -d 'Do not show at startup'
complete -c ro-start -l locale -d 'Set interface language' -xa 'en_US tr_TR de es fr it ja ru zh'
complete -c ro-start -s d -l debug -d 'Enable debug logging'
