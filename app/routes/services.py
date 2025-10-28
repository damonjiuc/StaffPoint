from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse

from app.config import settings
from app.services.regions import url_for_service, get_region, regions

templates = settings.configure_templates()

services_router = APIRouter(
    tags=['Services']
)




@services_router.get('/merch/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/merch/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/merch.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/merch-beauty/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/merch-beauty/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/merch-beauty.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/merch-diy/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/merch-diy/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/merch-diy.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/merch-meds/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/merch-meds/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/merch-meds.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/posm-placement/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/posm-placement/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/posm-placement.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/merch-tech/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/merch-tech/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/merch-meds.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/learning/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/learning/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/posm-learning.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/outsource-staff/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/outsource-staff/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/outsource-staff.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/outsource-sales/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/outsource-sales/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/outsource-sales.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/audit/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/audit/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/audit.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/retail-audit/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/retail-audit/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/retail-audit.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })


@services_router.get('/mystery/', response_class=HTMLResponse)
@services_router.get('/{region_slug}/mystery/', response_class=HTMLResponse)
async def index_page(request: Request, region_slug: str | None = None):
    region = get_region(region_slug)
    print("region resolved:", region)
    return templates.TemplateResponse('services/mystery.html', {
        'request': request,
        'region': region,
        'regions': regions,
        'url_for_service' : url_for_service
    })
