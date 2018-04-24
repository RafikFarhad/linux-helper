function homestead() {
    ( cd ~/Homestead && vagrant $* )
}

alias vu='homestead up'
alias vs='homestead ssh'
alias vh='homestead halt'
alias vp='homestead reload --provision'

alias gss='git status'
alias gb='git branch'
alias ga='git add .'
alias gc='git commit'
alias gcl='git clone'
alias gp='git push'
alias gpl='git pull'

alias hh='cd ~/html'
alias ii='cd ~/html/infancy'
alias root='cd ~/'
alias cc='ssh cse@103.84.159.232'

alias dcu='docker-compose up -d'
alias dcd='docker-compose down'
alias dcl='docker-compose logs -f'

