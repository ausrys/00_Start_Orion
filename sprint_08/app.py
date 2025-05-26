import re
import time

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


app = FastAPI()


# --------- Input Schema ---------
class SearchRequest(BaseModel):
    url: str
    search: str


# --------- Custom Exception ---------
class SearchNotFoundException(Exception):
    def __init__(self, message: str, error_code: int = 404):
        self.message = message
        self.error_code = error_code


@app.exception_handler(SearchNotFoundException)
async def search_not_found_handler(_: Request,
                                   exc: SearchNotFoundException):
    return HTTPException(status_code=exc.error_code, detail=exc.message)


# --------- Utility Functions ---------
def grab_text_from_url(url: str) -> str:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    text = driver.find_element(By.TAG_NAME, "body").text
    driver.quit()
    return text


def clean_text(text: str) -> str:
    return ''.join(c for c in text if c.isprintable())


def search_in_text(text: str, pattern: str):
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    if not matches:
        raise SearchNotFoundException(
            f"No matches found for pattern: '{pattern}'", 404)
    return matches


# --------- FastAPI Endpoint ---------
@app.post("/search")
def search_endpoint(data: SearchRequest):
    try:
        raw_text = grab_text_from_url(data.url)
        cleaned_text = clean_text(raw_text)

        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        matches = search_in_text(cleaned_text, data.search)
        return {"matches": matches}

    except SearchNotFoundException as e:
        raise HTTPException(status_code=e.error_code, detail=e.message) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
