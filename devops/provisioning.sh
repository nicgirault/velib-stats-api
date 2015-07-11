# on Ubuntu-Server-14.04LTS(trusty)-amd64

sudo apt-get update
sudo apt-get install postgresql-client
sudo apt-get install postgresql postgresql-contrib

set -a
source .env # TO BE WRITTEN with $DB_PASSWORD

sudo -u postgres psql postgres -c "create user api with password '$DB_PASSWORD';"
sudo -u postgres psql postgres -c "create database velib_statistics;"
sudo -u postgres psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE velib_statistics to api;"

# psql -d velib_statistics -U api -p5432 -hlocalhost -W

sudo apt-get install git python-pip libpq-dev python3-dev nginx
sudo pip install virtualenv


sudo mkdir /var/www && cd /var/www
sudo chown -R ubuntu:ubuntu /var/www

git clone --recursive git@github.com:nicgirault/velib-stats-api.git && cd velib-stats-api
sudo cp devops/nginx.conf /etc/nginx/site-available/velib
sudo ln -s /etc/nginx/sites-available/velib /etc/nginx/sites-enabled/
sudo service nginx reload
sudo service nginx restart


virtualenv venv -p /usr/bin/python3
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt --upgrade

export PYTHONPATH=src:test
