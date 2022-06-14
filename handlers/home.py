from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from depends.collector import get_current_user

templates = Jinja2Templates(directory="templates")
routing = APIRouter()


@routing.get("/", response_class=HTMLResponse)
async def static_content(request: Request, current_user=Depends(get_current_user)):
    return templates.TemplateResponse("home.html", {"request": request})
