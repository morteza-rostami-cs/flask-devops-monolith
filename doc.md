```bash

pip install Flask

pip freeze > api/requirements.txt

# we install from requirements.txt
# in there we write: Flask -- and when we run this command, it installs every dependency
pip install -r requirements.txt

# run flask
flask --app api.src.app run --debug

tree -a -I ".venv|.git"

## postgres setup=========================

sudo -u postgres psql

# list databases
\l

# list users
\du

# connect to a db
\c database_name

# show tables
\dt

# show which db we are connected to
\conninfo

# exit
\q

## redis=================

sudo systemctl status redis-server
sudo systemctl start redis-server
redis-cli ping

## rabbitMQ =============

sudo apt update
sudo apt install rabbitmq-server
sudo systemctl status rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo rabbitmqctl status

# install this pip package
pika

# run our worker script
python -m worker.producer

# lets add path for rabbitmq plugins folder
    sudo nano /etc/rabbitmq/rabbitmq-env.conf
    # add this at the end
    PLUGINS_DIR="/usr/lib/rabbitmq/lib/rabbitmq_server-4.0.5/plugins"

    # reset
    sudo systemctl restart rabbitmq-server

    # check cli has access to plugins
    sudo rabbitmq-plugins list

# now: enable plugin -- for http the GUI tool to work
sudo rabbitmq-plugins enable rabbitmq_management

# now check if port 15672 is open? -- this is for http GUI connection
sudo ss -tulpn | grep 15672

# if you see this -- port is open and gui works
pax@apax-virtualbox:~/spaces/11_devops_py/flask-devops-monolith$ sudo ss -tulpn | grep 15672
tcp   LISTEN 0      1024         0.0.0.0:15672      0.0.0.0:*    users:(("beam.smp",pid=532216,fd=43))

# pika can access it on a different port
RABBITMQ_URL=amqp://guest:guest@localhost:5672/


```
