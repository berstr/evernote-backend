# evernote-backend

# based on https://github.com/evernote/evernote-sdk-python3

## Env Variables

    export NEW_RELIC_LICENSE_KEY=XXXX

    export NEW_RELIC_APP_NAME=evernote-backend

    export NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
    export NEW_RELIC_APPLICATION_LOGGING_ENABLED=true
    export NEW_RELIC_APPLICATION_LOGGING_FORWARDING_ENABLED=true

    export EVERNOTE_AUTH_TOKEN=<TOKEN>
    export EVERNOTE_PORT=XXX                Note: Default port id 37071

Optional - if you run front-end stand-alone (backend either via docker or CLI)

    export EVERNOTE_BACKEND_CORS=true

## CLI

Manual start from command line:

export PYTHONPATH=./lib; newrelic-admin run-program gunicorn -w 4 -b 0.0.0.0:37071 evernote_backend:APP

Old: export PYTHONPATH=./lib; newrelic-admin run-program python3 evernote_backend.py

---------------------

## Docker

X.Y is the image tag

    docker build -t bstransky/evernote:X.Y .

    docker run -d --name evernote -e NEW_RELIC_LICENSE_KEY -e NEW_RELIC_DISTRIBUTED_TRACING_ENABLED -e NEW_RELIC_APPLICATION_LOGGING_ENABLED -e NEW_RELIC_APPLICATION_LOGGING_FORWARDING_ENABLED -e NEW_RELIC_APP_NAME  -e EVERNOTE_AUTH_TOKEN -e EVERNOTE_PORT -v $(pwd)/logs:/logs -p37071:37071 bstransky/evernote:X.Y
