#!/bin/bash
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'
echo  "${CYAN}Welcome to Easy LEMP Stack Setup${NC}"
echo  "${CYAN}Ubuntu 18.04 Supported${NC}"

echo  "${GREEN}Created By SUST CSE Developer Network (SCDN)\n${NC}"
echo  "${GREEN}Maintained By Rafik Farhad\n${NC}"

echo "${CYAN}Steap:1 [System Update]${NC}"
echo "${CYAN}Update Starts.....${NC}"
sudo apt-get update
echo  "${GREEN}System Update Completed Successfully\n${NC}"

echo "${CYAN}Step:2 [Install NGINX]${NC}"
sudo apt-get install -y nginx
echo  "${GREEN}NGINX Installation Completed Successfully\n${NC}"

echo "${CYAN}Step:3 [Install MySQL]${NC}"
sudo apt-get install -y mysql-server mysql-client libmysqlclient-dev
echo  "${GREEN}MySQL Installation Completed Successfully\n${NC}"

echo "${CYAN}Step:4 [Install PHP7.2]${NC}"
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:ondrej/php -y 
sudo apt-get -y update
sudo apt-get install -y php7.2
udo apt-cache search php7.2
sudo apt-get install -y php-GREENis php7.2-cli php7.2-fpm php7.2-mysql php7.2-curl php7.2-json php7.2-cgi libphp7.2-embed libapache2-mod-php7.2 php7.2-zip php7.2-mbstring php7.2-xml php7.2-intl

echo  "${GREEN}PHP 7.2 Installation Completed Successfully\n${NC}"

sudo systemctl start php7.2-fpm
sudo systemctl enable php7.2-fpm

echo "${CYAN}Step:5 [Install PHPmyadmin]${NC}"
wget https://files.phpmyadmin.net/phpMyAdmin/4.7.9/phpMyAdmin-4.7.9-all-languages.zip -O ./phpmyadmin.zip
sudo unzip phpmyadmin.zip -d /home/$USER/html
sudo mv phpMyAdmin-4.7.9-all-languages /home/$USER/html/phpmyadmin
sudo chown -R www-data:www-data /home/$USER/html/phpmyadmin/
sudo chmod -R 755 /home/$USER/html/phpmyadmin
echo  "${GREEN}PHPmyadmin Installation Completed Successfully\n${NC}"

sudo systemctl restart nginx

echo "${CYAN}Remove the default symlink in sites-enabled directory${NC}"
sudo rm /etc/nginx/sites-enabled/default
sudo cat > /etc/nginx/sites-enabled/default.conf <<EOF
server {
   listen 80;
   #listen [::]:80;
   root /home/$USER/html;
   index index.php index.html index.htm index.nginx-debian.html;
   server_name localhost;

   location / {
       try_files \$uri \$uri/ /index.php?\$query_string;
   }

location ~ \.php$ {
    #NOTE: You should have "cgi.fix_pathinfo = 0;" in php.ini
    include fastcgi_params;                
    fastcgi_intercept_errors on;
    fastcgi_pass unix:/run/php/php7.2-fpm.sock;
    fastcgi_param SCRIPT_FILENAME $document_root/\$fastcgi_script_name;
}
   location ~ /\.ht {
       deny all;
   }
}
EOF
sudo mkdir /home/$USER/html/
sudo cp /usr/share/nginx/html/index.html /home/$USER/html/
sudo chown -R www-data:www-data /home/$USER/html
sudo nginx -t
sudo systemctl reload nginx
sudo systemctl restart nginx
echo  "${GREEN}NGINX Setup complete${NC}"

echo "${CYAN}Step:6 [Install curl]${NC}"
sudo apt-get install -y curl
echo  "${GREEN}curl Installation Completed Successfully\n${NC}"

echo "${CYAN}Step:7 [Install Git]${NC}"
sudo add-apt-repository ppa:git-core/ppa -y
sudo apt-get update
sudo apt-get install -y git
echo  "${GREEN}Git Installation Completed Successfully\n${NC}"

echo "${CYAN}Step:8 [Install Composer]${NC}"
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
echo  "${GREEN}Composer Installation Completed Successfully\n${NC}"

echo "${CYAN}Step:9 [NodeJS and npm]${NC}"
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
echo  "${GREEN}NodeJS and npm install complete${NC}"

echo "${CYAN}Thanks  !!!${NC}"
