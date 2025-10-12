from fastapi import FastAPI

from app.core.config import configs
from app.api.v1 import subapp as v1_app
from app.core.container import Container


class AppIni:
    def __init__(self) -> None:
        self.app = FastAPI( title = configs.projectcfg.project_name )

        # Container
        self.container = Container()

        # Database

		# Mount subapps
        self.app.mount("/v1", v1_app)


containerIni = AppIni()
app = containerIni.app