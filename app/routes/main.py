from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse

from app.config import settings
from app.services.regions import url_for_service, get_region, regions

templates = settings.configure_templates()

main_router = APIRouter(
    tags=['Main']
)


@main_router.get("/favicon.ico")
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")


@main_router.get('/', response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request,
        'region': None,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@main_router.get('/merch/', response_class=HTMLResponse)
@main_router.get('/{region_slug}/merch/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('merch.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@main_router.get('/outsource/', response_class=HTMLResponse)
@main_router.get('/{region_slug}/outsource/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    return templates.TemplateResponse('outsource.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@main_router.get('/{region_slug}/', response_class=HTMLResponse)
async def index_page_region(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    return templates.TemplateResponse('index.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })