FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD [ "python", "-m", "api.v1.app" ]

EXPOSE 5000