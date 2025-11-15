"""
Service layer for the URL shortener application.
"""
import string
import random
from typing import Optional
from database.url import URLDB

class URLShortnerService:
    """
    Provides functionality for creating and retrieving short URLs.
    """
    def __init__(self) -> None:
        self.urldb: URLDB = URLDB()

    def get_long_url(self, short_url: str) -> Optional[str]:
        """
        Retrieves the long URL associated with a given short URL.

        Args:
            short_url: The short URL to look up.

        Returns:
            The corresponding long URL, or None if not found.
        """
        return self.urldb.get_url_record(short_url)

    def create_short_url(self, long_url: str) -> str:
        """
        Creates a short URL for a given long URL and stores it.

        Args:
            long_url: The long URL to shorten.

        Returns:
            The generated short URL.
        """
        short_url = self.generate_short_url()
        while self.urldb.short_url_exists(short_url):
            short_url = self.generate_short_url()

        record = {
            "url": long_url,
            "short_url": short_url,
        }
        self.urldb.insert_url_record(record)
        return short_url

    def generate_short_url(self, length: int = 6) -> str:
        """
        Generates a random short URL of a specified length.

        Args:
            length: The desired length of the short URL. Defaults to 6.

        Returns:
            A randomly generated short URL string.
        """
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
