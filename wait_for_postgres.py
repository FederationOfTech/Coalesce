import os
import logging
from time import time, sleep
import psycopg2
import dj_database_url

check_timeout = os.getenv("POSTGRES_CHECK_TIMEOUT", 30)
check_interval = os.getenv("POSTGRES_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"

# Get the database connection details from DATBASE_URL
django_db_config = dj_database_url.config()

config = {
    "dbname": django_db_config.get("NAME", "postgres"),
    "user": django_db_config.get("USER", "postgres"),
    "password": django_db_config.get("PASSWORD", "postgres"),
    "host": django_db_config.get("HOST", "postgres")
}

start_time = time()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def pg_isready(host, user, password, dbname):
    while time() - start_time < check_timeout:
        try:
            conn = psycopg2.connect(**vars())
            logger.info("Postgres is ready! ✨ 💅")
            conn.close()
            return True
        except psycopg2.OperationalError:
            logger.info(f"Postgres isn't ready. Waiting for {check_interval} {interval_unit}...")
            sleep(check_interval)

    logger.error(f"We could not connect to Postgres within {check_timeout} seconds.")
    return False


pg_isready(**config)
