from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schemes.doctor_schema import DoctorSchema, DoctorCreateRequest, DoctorUpdateRequest, DoctorChangePatientsRequest
from app.schemes.filters import Pagination



router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.get("/", summary="Get list doctors")
@inject
def get_list(pag = Depends(Pagination), service = Depends(Provide[Container.doctor_service])) -> list[DoctorSchema]:
    return service.get_list(pag)


@router.get("/{id}", summary="Get doctor by id")
@inject
def get_doctor_by_id(id:int, service = Depends(Provide[Container.doctor_service])) -> DoctorSchema:
    return service.get_by_id_with_many2many(id)


@router.post("/", summary="Create doctor", status_code=201)
@inject
def create_doctor(schema: DoctorCreateRequest, service = Depends(Provide[Container.doctor_service])) -> DoctorSchema:
    return service.create(schema)


@router.put("/{id}", summary="Full doctor update", status_code=200)
@inject
def full_doctor_update(id:int, schema:DoctorUpdateRequest, service = Depends(Provide[Container.doctor_service])) -> DoctorSchema:
    return service.full_update(id, schema)


@router.patch("/{id}", summary="Partial doctor update", status_code=200)
@inject
def partial_doctor_update(id:int, schema:DoctorUpdateRequest, service = Depends(Provide[Container.doctor_service])) -> DoctorSchema:
    return service.partial_update(id, schema)


@router.post("/{id}/patient/add", summary="Add patient to doctor", status_code=200)
@inject
def add_patient_to_doctor(id:int, schema:DoctorChangePatientsRequest, service = Depends(Provide[Container.doctor_service])) -> None:
    return service.add_patient(id, schema.patient_id)


@router.delete("/{id}/patient/delete", summary="Delete patient from doctor", status_code=200)
@inject
def remove_patient_from_doctor(id:int, schema:DoctorChangePatientsRequest, service = Depends(Provide[Container.doctor_service])) -> None:
    return service.remove_patient(id, schema.patient_id)


@router.delete("/{id}", summary="Delete doctor", status_code=204)
@inject
def delete_doctor(id:int, service = Depends(Provide[Container.doctor_service])) -> None:
    return service.delete(id)