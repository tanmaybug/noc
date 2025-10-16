from fastapi import APIRouter

from controllers.V1 import registration_controller
from controllers.V1 import login_controller
from controllers.V1 import noc_application_controller

master_router = APIRouter()

master_router.include_router(registration_controller.router,prefix="/v1")
master_router.include_router(login_controller.router, prefix="/v1")
master_router.include_router(noc_application_controller.router, prefix="/v1")