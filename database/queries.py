INSERT_URL_RECORD = """
INSERT INTO urls (url, short_url, created_at, request_count)
VALUES (?, ?, ?, ?)
"""

UPDATE_REQUEST_COUNT = """
UPDATE urls
SET request_count = ?
WHERE url = ?
"""