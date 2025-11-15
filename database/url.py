"""
Database operations for the URL shortening service.
"""
import datetime
from typing import Optional

from .db import Database
from .queries import INSERT_URL_RECORD, UPDATE_REQUEST_COUNT

class URLDB:
    """
    Handles database interactions for URL records.
    """
    def __init__(self) -> None:
        self.db = Database()
        self._create_table()


    def _create_table(self) -> None:
        """
        Creates the 'urls' table if it does not already exist.
        """
        with self.db.get_connection() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL,
                    short_url TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    request_count INTEGER NOT NULL
                )
            """)

    def insert_url_record(self, record: dict) -> None:
        """
        Inserts a new URL record into the database.

        Args:
            record: A dictionary containing 'url' and 'short_url'.
        """
        created_at = str(datetime.datetime.now())
        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(INSERT_URL_RECORD, (record['url'], record['short_url'], created_at, 0))

    def get_url_record(self, short_url: str) -> Optional[str]:
        """
        Retrieves the long URL for a given short URL and updates the request count.

        Args:
            short_url: The short URL to look up.

        Returns:
            The corresponding long URL, or None if not found.
        """
        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT url FROM urls WHERE short_url = ?", (short_url,))
            record = cursor.fetchone()
        if record:
            self.update_request_count(record[0])
            return record[0]
        return None

    def short_url_exists(self, short_url: str) -> bool:
        """
        Checks if a short URL already exists in the database.

        Args:
            short_url: The short URL to check.

        Returns:
            True if the short URL exists, False otherwise.
        """
        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT 1 FROM urls WHERE short_url = ?", (short_url,))
            return cursor.fetchone() is not None

    def update_request_count(self, url: str) -> None:
        """
        Increments the request count for a given URL.

        Args:
            url: The long URL whose request count needs to be updated.
        """
        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT request_count FROM urls WHERE url = ?", (url,))
            record = cursor.fetchone()
            if record:
                new_count = record[0] + 1
                cursor.execute(UPDATE_REQUEST_COUNT, (new_count, url))
