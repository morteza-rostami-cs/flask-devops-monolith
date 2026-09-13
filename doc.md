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

# redis cli

redis-cli
127.0.0.1:6379> SET name ali
OK
127.0.0.1:6379> GET name
"ali"
127.0.0.1:6379> DEL name
(integer) 1
127.0.0.1:6379> GET name
(nil)
127.0.0.1:6379> exit

# Redis keys

# A common Redis convention is to structure keys using :.

# For example:

# user:1
# user:2
# user:3

```
