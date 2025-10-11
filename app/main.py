from fastapi import FastAPI

from app.core.config import configs
from app.api.v1 import subapp as v1_app


class AppIni:
    def __init__(self) -> None:
        self.app = FastAPI( title = configs.projectcfg.project_name )

        # Container

        # Database

		# Mount subapps
        self.app.mount("/v1", v1_app)


containerIni = AppIni()
app = containerIni.app