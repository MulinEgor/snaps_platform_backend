from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config import APIConfig


if __name__ == "__main__":
    # Loading environment variables
    load_dotenv()
    
    # Configuration API
    config = APIConfig()
    app = FastAPI(
        **config.model_dump()
    )
    app.add_middleware(
        CORSMiddleware,
        **config.cors.model_dump()
    )

    # Your routes here
    routers = []
    for router in routers:
        app.include_router(router)
        