FROM python:3.12.3

WORKDIR /app

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /app/scripts/init.sh
RUN chmod +x /app/scripts/start.sh