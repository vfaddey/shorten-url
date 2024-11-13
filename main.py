import code

from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import RedirectResponse

from schemas import URLResponse, URLRequest
from url_service import URLService

app = FastAPI()


@app.get("/{short_url}")
async def redirect_to(short_url: str,
                      url_service: URLService = Depends()):
    redirect_url = await url_service.get_by_short_url(short_url)
    if redirect_url:
        return RedirectResponse(redirect_url.long_url)
    raise HTTPException(status_code=404)

@app.post('/', response_model=URLResponse)
async def shorten_url(request: URLRequest,
                      url_service: URLService = Depends()):
    result = await url_service.shorten_url(request.long_url)
    return URLResponse(long_url=request.long_url, short_url=result)