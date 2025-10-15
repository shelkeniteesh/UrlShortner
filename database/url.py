import datetime

from .db import Database
from .queries import INSERT_URL_RECORD, UPDATE_REQUEST_COUNT

class URLDB:
    def __init__(self):
        self.db = Database()

    def insert_url_record(self, record):
        modified_at = str(datetime.datetime.now())
        self.db.connection.execute()

    def update_request_count(self, record):
        