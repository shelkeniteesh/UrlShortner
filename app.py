"""
FastAPI application for URL shortening service.
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from service.url_shortner_service import URLShortnerService

app = FastAPI()
url_shortener_service = URLShortnerService()

class URL(BaseModel):
    """
    Pydantic model for URL input.
    """
    long_url: str

@app.get("/{short_url}")
def redirect_to_long_url(short_url: str):
    """
    Redirects a short URL to its corresponding long URL.

    Args:
        short_url: The short URL to redirect.

    Returns:
        A RedirectResponse to the long URL.

    Raises:
        HTTPException: If the short URL is not found (404).
    """
    long_url = url_shortener_service.get_long_url(short_url)
    if long_url:
        return RedirectResponse(url=long_url)
    raise HTTPException(status_code=404, detail="URL not found")

@app.post("/shorten")
def create_short_url(url: URL):
    """
    Creates a short URL for a given long URL.

    Args:
        url: A URL object containing the long URL.

    Returns:
        A dictionary containing the generated short URL.
    """
    short_url = url_shortener_service.create_short_url(url.long_url)
    return {"short_url": short_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
