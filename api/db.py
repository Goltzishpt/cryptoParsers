import glob
import logging
import asyncio
import asyncpg
from settings import config
from asyncpg.exceptions import DuplicateDatabaseError

logging.getLogger(__name__)


async def connect_create_if_not_exists(user, database):
    try:
        conn = await asyncpg.connect(config.db_uri)
    except asyncpg.InvalidCatalogNameError:
        # Database does not exist, create it.
        sys_conn = await asyncpg.connect(
            database='postgres',
            password=config.POSTGRES_PASSWORD,
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.POSTGRES_USER
        )
        try:
            await sys_conn.execute(
                f'CREATE DATABASE "{database}" OWNER "{user}";'
            )
            await sys_conn.close()
        except DuplicateDatabaseError:
            logging.info(f'DATABASE {config.POSTGRES_DB} already createds')
        # Connect to the newly created database.
        conn = await asyncpg.connect(config.db_uri)

    return conn


async def run():
    conn = await connect_create_if_not_exists(config.POSTGRES_USER, config.DB_NAME)
    for i in sorted(glob.glob("./sql/*.sql"), reverse=True):
        with open(i, 'r') as sql_script:
            await conn.execute(sql_script.read())


if __name__ == "__main__":
    logging.info('Init sql script to db')
    asyncio.new_event_loop().run_until_complete(run())
    logging.info('Finish run sql script')
