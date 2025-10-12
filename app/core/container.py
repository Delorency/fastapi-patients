from dependency_injector import containers, providers

from .database import Database
from .config import configs
from repos import *
from services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            
        ]
    )

    # Database
    database = providers.Singleton(Database, uri=configs.dbcfg.database_uri)


    # Repos
    doctor_repo = providers.Factory(DoctorRepo, session=database.provided.session)
    patient_repo = providers.Factory(PatientRepo, session=database.provided.session)


    # Services
    doctor_service = providers.Factory(DoctorService, repo=doctor_repo)
    patient_service = providers.Factory(PatientService, repo=patient_repo)