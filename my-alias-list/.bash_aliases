function homestead() {
    ( cd ~/Homestead && vagrant $* )
}

alias vu='homestead up'
alias vs='homestead ssh'
alias vh='homestead halt'
alias vp='homestead reload --provision'

alias gss='git status'
alias gb='git branch'
alias ga='git add'
alias gc='git commit'
alias gcl='git clone'
alias gp='git push'
alias gpl='git pull'

alias hh='cd ~/html'
alias ii='cd ~/html/infancy'
alias root='cd ~/'

