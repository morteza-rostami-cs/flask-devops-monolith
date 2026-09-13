import psycopg
from psycopg_pool import ConnectionPool
from shared.settings import settings
from collections.abc import Callable

# init the db connection pool once
pool: ConnectionPool = ConnectionPool(settings.DATABASE_URL)

type DBPool = ConnectionPool
type GetDb = Callable[[], DBPool]


# get connection pool
def get_pool():
    return pool


# for open and close connection
def get_connection():
    """create and return a db connection"""
    return psycopg.connect(settings.DATABASE_URL)
