from dependency_injector import containers, providers

from .database import Database
from .config import configs
from app.repos import *
from app.services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.patient_api",
            "app.api.v1.endpoints.doctor_api"
        ]
    )

    # Database
    database = providers.Singleton(Database, uri=configs.dbcfg.database_uri)


    # Repos
    patient2doctor_repo = providers.Factory(Patient2DoctorRepo, session=database.provided.session)
    bmr_repo = providers.Factory(BMRRepo, session=database.provided.session)
    doctor_repo = providers.Factory(DoctorRepo, session=database.provided.session, p2d=patient2doctor_repo)
    patient_repo = providers.Factory(PatientRepo, session=database.provided.session, p2d=patient2doctor_repo, bmr=bmr_repo)

    # Services
    doctor_service = providers.Factory(DoctorService, repo=doctor_repo)
    patient_service = providers.Factory(PatientService, repo=patient_repo)