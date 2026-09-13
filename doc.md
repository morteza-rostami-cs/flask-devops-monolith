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

```
