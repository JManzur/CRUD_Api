FROM python:3.9

WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
COPY app.py /usr/src/app/
COPY .env /usr/src/app/
COPY log_conf.yml /usr/src/app/
ADD config /usr/src/app/config
ADD models /usr/src/app/models
ADD routes /usr/src/app/routes
ADD schemas /usr/src/app/schemas
ADD landing_page /usr/src/app/landing_page
ADD middleware /usr/src/app/middleware

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

EXPOSE 8082

# ENV AWS_DEFAULT_REGION=us-east-1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8082", "--log-config", "log_conf.yml"]