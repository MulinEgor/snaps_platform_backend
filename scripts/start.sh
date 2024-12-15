# run seeds
python -m seeds.main
# start API
uvicorn api.main:app --host ${API_HOST} --port ${API_PORT} 
