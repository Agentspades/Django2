echo Script started
sudo su
apt update && apt upgrade
echo Installing pip
apt install python3-pip
echo CLoning source
git clone https://github.com/agentspades/Django2.git
echo Installing MySQL
apt install mysql-server
echo Setting up MySQL
mysql_secure_installation
echo Creating table
mysql
CREATE DATABASE TAFESDG;
exit
cd Djano2/app
echo installing dependencies
apt install python3-dev build-essential
apt install libssl1.1
apt install libssl1.1=1.1.1f-1ubuntu2
apt install libssl-dev
apt install libmysqlclient-dev
pip3 install mysqlclient
pip3 install -r reqs.txt
echo Script complete now edit settings.py and run setup-server.sh
