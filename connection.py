import os
from dotenv import load_dotenv

load_dotenv()

import psycopg2 as psql

postgres_conn = psql.connect(
    host = os.getenv("DATABASE_HOST"),
    database = os.getenv("DATABASE_NAME"),
    user = os.getenv("DATABASE_USER"),
    password = os.getenv("DATABASE_PASSWORD")
)


