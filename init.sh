python -m prisma generate
python -m prisma db push 
uvicorn api.main:app --host ${API_HOST} --port ${API_PORT}
