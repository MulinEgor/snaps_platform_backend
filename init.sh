python -m prisma generate
python -m prisma db push --accept-data-loss
uvicorn api.main:app --host ${API_HOST} --port ${API_PORT} 
