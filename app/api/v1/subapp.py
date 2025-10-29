from fastapi import FastAPI
from .endpoints import *


subapp = FastAPI()

routers = [
    patient_router,
    doctor_router
]

for router in routers:
    subapp.include_router(router)