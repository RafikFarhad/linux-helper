#!/bin/bash
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo "${CYAN}-  Stopping MYSQL  -${NC}"
sudo service mysql stop
echo "${CYAN}-  Creating Temp Directory  -${NC}"
sudo mkdir -p /var/run/mysqld
sudo chown mysql:mysql /var/run/mysqld
echo "${CYAN}-  Starting Service  -${NC}"
sudo /usr/sbin/mysqld --skip-grant-tables --skip-networking &
echo "${CYAN}-  Checking Service  -${NC}"
jobs
echo "${CYAN}-  Start MySql in safe mood  -${NC}"
mysql -u root

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)
mysql> SET PASSWORD FOR root@'localhost' = PASSWORD('linuxconfig.org');
Query OK, 0 rows affected, 1 warning (0.00 sec)
mysql> quit     
echo "${CYAN}-   -${NC}"
sudo pkill mysqld            
echo "${CYAN}-   -${NC}"
sudo service mysql start
echo "${CYAN}-   -${NC}"
echo "${CYAN}-   -${NC}"
echo "${CYAN}-   -${NC}"
echo "${CYAN}-   -${NC}"
echo "${CYAN}-   -${NC}"