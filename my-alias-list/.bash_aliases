function homestead() {
    ( cd ~/Homestead && vagrant $* )
}

function enter() {
    ( docker exec -it $* bash )
}

alias vu='homestead up'
alias vs='homestead ssh'
alias vh='homestead halt'
alias vp='homestead reload --provision'

alias gss='git status'
alias gch='git checkout'
alias ga='git add --all'
alias gc='git commit -m'
alias gcl='git clone'
alias gp='git push'
alias gpl='git pull'
alias gct='git checkout'

alias ddh='cd ~/Desktop'
alias hh='cd ~/html'
alias ii='cd ~/html/infancy'
alias root='cd ~/'
alias cc='ssh cse@103.84.159.232'
alias cse='ssh root@103.84.159.8'

alias cu='composer update'
alias pa='php artisan'
alias pacc='php artisan config:cache'
alias pakg='php artisan key:generate'

alias dcu='docker-compose up -d'
alias dcd='docker-compose down'
alias dcl='docker-compose logs -f'
alias dps='docker ps'
alias dim='docker image'
alias ds='docker stop'
alias drm='docker rm'

