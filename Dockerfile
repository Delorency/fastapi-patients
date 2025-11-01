FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

RUN chmod +x entrypoint.sh

CMD ["sh", "./entrypoint.sh"]