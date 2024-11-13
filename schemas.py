from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    long_url: HttpUrl


class URLResponse(BaseModel):
    long_url: HttpUrl
    short_url: str