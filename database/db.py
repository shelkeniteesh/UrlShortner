"""
Database connection utility for the URL shortening service.
"""
import os
import sqlite3
from dotenv import load_dotenv
from fastapi import Depends

load_dotenv()

class Database:
    """
    Provides access to the SQLite database file.
    """
    def __init__(self):
        """
        Stores the path to the database file supplied via environment variable.
        """
        path = os.environ.get('DATABASE_FILE_PATH')
        if not path:
            raise RuntimeError("DATABASE_FILE_PATH is not set in the environment.")
        self._db_path = path

    def get_connection(self) -> sqlite3.Connection:
        """
        Returns a new sqlite3 connection that can be used safely per thread.
        """
        return sqlite3.connect(self._db_path, check_same_thread=False)

    def close(self):
        """
        Placeholder to keep the API compatible; connections are short-lived.
        """
