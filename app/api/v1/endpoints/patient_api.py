from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schemes.filters import FullNameFilter, AgeFilter, GenderFilter
from app.schemes.patient_schema import PatientSchema, PatientCreateRequest, PatientUpdateRequest, \
    PatientChangeDoctorsRequest, PatientGetListSchema 
from app.schemes.filters import Pagination



router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/", summary="Get list patients")
@inject
def get_list(
    pag = Depends(Pagination), 
    full_name_filter = Depends(FullNameFilter),
    age_filter = Depends(AgeFilter),
    gender_filter = Depends(GenderFilter),
    service = Depends(Provide[Container.patient_service])) -> list[PatientGetListSchema]:
    return service.get_list_with_filters(pag, full_name_filter, age_filter, gender_filter)


@router.get("/{id}", summary="Get patient by id")
@inject
def get_patient_by_id(id:int, service = Depends(Provide[Container.patient_service])) -> PatientSchema:
    return service.get_by_id_with_many2many(id)


@router.post("/", summary="Create patient", status_code=201)
@inject
def create_patient(schema: PatientCreateRequest, service = Depends(Provide[Container.patient_service])) -> PatientSchema:
    return service.create(schema)


@router.put("/{id}", summary="Full patient update", status_code=200)
@inject
def full_patient_update(id:int, schema:PatientUpdateRequest, service = Depends(Provide[Container.patient_service])) -> PatientSchema:
    return service.full_update(id, schema)


@router.patch("/{id}", summary="Partial patient update", status_code=200)
@inject
def partial_patient_update(id:int, schema:PatientUpdateRequest, service = Depends(Provide[Container.patient_service])) -> PatientSchema:
    return service.partial_update(id, schema)


@router.delete("/{id}", summary="Delete patient", status_code=204)
@inject
def delete_patient(id:int, service = Depends(Provide[Container.patient_service])) -> None:
    return service.delete(id)


@router.post("/{id}/doctor/add", summary="Add doctor to patient", status_code=200)
@inject
def add_doctor_to_patient(id:int, schema:PatientChangeDoctorsRequest, service = Depends(Provide[Container.patient_service])) -> None:
    return service.add_doctor(id, schema.doctor_id)


@router.delete("/{id}/doctor/delete", summary="Delete doctor from patient", status_code=200)
@inject
def remove_doctor_to_patient(id:int, schema:PatientChangeDoctorsRequest, service = Depends(Provide[Container.patient_service])) -> None:
    return service.remove_doctor(id, schema.doctor_id)
