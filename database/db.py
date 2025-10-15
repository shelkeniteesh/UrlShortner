import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(os.environ.get('DATABASE_FILE_PATH'))
