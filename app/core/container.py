from dependency_injector import containers, providers

from .database import Database
from .config import configs


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            
        ]
    )

    # Database
    database = providers.Singleton(Database, uri=configs.dbcfg.database_uri)


    # Repos


    # Services