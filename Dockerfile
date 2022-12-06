# FROM python:3.11.0-slim AS base

FROM python:3.9-alpine AS base

RUN pip install --no-cache-dir newrelic

ENTRYPOINT ["newrelic-admin", "run-program"]

FROM base AS final

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV NEW_RELIC_LOG=stdout
ENV PYTHONPATH=./lib:./modules; 
CMD [ "python3", "evernote_backend.py"]