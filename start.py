import uvicorn
from app.core.config import configs



if __name__ == '__main__':
    uvicorn.run(
        "app.main:app",
        host = configs.servercfg.host,
        port = configs.servercfg.port,
        log_level="info",
        reload=True
    )