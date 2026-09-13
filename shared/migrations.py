from pathlib import Path
import psycopg
from psycopg import sql
from typing import LiteralString, cast

from shared.settings import settings

# path to migration folder
# __file__ :: path to current file
# resolve() :: make absolute path
# parent :: go on dir up
MIGRATIONS_DIR = Path(__file__).resolve().parent.parent / "migrations"


# create migrations table once
# store migrations we run -- here
def ensure_migrations_table():
    # use 0001_create_users as primary key
    with psycopg.connect(settings.DATABASE_URL) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version TEXT PRIMARY KEY,
                applied_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            )
        """)


# return all used migrations
def get_applied_migrations():
    with psycopg.connect(settings.DATABASE_URL) as conn:
        rows = conn.execute("""
            SELECT version
            FROM schema_migrations
            ORDER BY version
        """).fetchall()

    # return a set of -- migrations names/versions
    return {row[0] for row in rows}


# run one migration
def run_migrations():
    # create migrations table -- if not exists
    ensure_migrations_table()
    # get applied migrations
    applied = get_applied_migrations()
    # return migrations .sql files (sorted)
    migration_files = sorted(MIGRATIONS_DIR.glob("*.sql"))

    for migration_file in migration_files:
        # get version or file name: eg: 001_something
        # stem: fileName without extension .sql
        version = migration_file.stem

        # if already applied -- skip
        if version in applied:
            print(f"Skipping {version}")
            continue

        print(f"Applying {version}...")
        # read sql file into a string
        sql_text: str = migration_file.read_text()

        try:
            with psycopg.connect(settings.DATABASE_URL) as conn:

                ## this is a transaction
                ## any of these .execute lines fails -- both role back

                # run raw sql against db
                conn.execute(sql.SQL(cast(LiteralString, sql_text)))

                # record this migration file as applied
                conn.execute(
                    """
                    INSERT INTO schema_migrations (version)
                    VALUES (%s)
                    """,
                    (version,),
                )

            print(f"Applied {version}")

        except Exception:
            print(f"Failed to apply {version}")
            raise


if __name__ == "__main__":
    run_migrations()
