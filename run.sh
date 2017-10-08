cd /src


python3 manage.py migrate
python3 manage.py collectstatic

sudo service nginx restart
sudo /etc/init.d/supervisor start myproject

sleep 600000