from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schemes.patient_schema import PatientSchema
from app.schemes.filters import Pagination


router = APIRouter("/patients", tags=["patients"])


@router.get("/", summary="Get list patients")
@inject
def get_list(pag = Depends(Pagination), service = Depends(Provide[Container.patient_service])) -> list[PatientSchema]:
    return service.get_list(pag)