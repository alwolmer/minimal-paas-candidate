from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, TypeAdapter, parse_obj_as
from dotenv import load_dotenv
import os

load_dotenv()
raw_link = os.getenv("EASTER_EGG_LINK", "https://example.com/")

adapter = TypeAdapter(HttpUrl)

try:
    EASTER_EGG_LINK = adapter.validate_python(raw_link)
except Exception:
    EASTER_EGG_LINK = adapter.validate_python("https://example.com/")

app = FastAPI()

class EasterEgg(BaseModel):
    message: str
    link: HttpUrl

@app.get("/", response_model=dict)
def read_root():
    return {"Hello": "World"}

@app.get("/easter_egg", response_model=EasterEgg)
def easter_egg():
    return EasterEgg(message="You found the Easter egg!", link=EASTER_EGG_LINK)