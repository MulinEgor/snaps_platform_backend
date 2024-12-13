from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config import APIConfig
from api.graphql_router import graphql_router


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


app.include_router(graphql_router, prefix="/graphql")
