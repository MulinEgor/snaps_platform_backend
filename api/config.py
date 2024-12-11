from pydantic import BaseModel


class CorsConfig(BaseModel):
    allow_origins: list[str] = ['*']
    allow_credentials: bool = True
    allow_methods: list[str] = ['*']
    allow_headers: list[str] = ['*']


class APIConfig(BaseModel):
    title: str = 'SNAPS platform API'
    root_path: str = '/api'
    docs_url: str = '/docs'
    cors: CorsConfig = CorsConfig()
