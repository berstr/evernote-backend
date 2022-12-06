from flask import Flask #, jsonify, request

import os
import logging
from logging.handlers import RotatingFileHandler

from evernote.api.client import EvernoteClient


# ==========================
# Constants
# ==========================
EVERNOTE_PORT_DEFAULT = 37071


# ==========================
# The following variables are being set by the application at runtime:
# ==========================
APP = None
LOGGER = None
EVERNOTE = None


# ==========================
# The following variables are set through env variables
# ==========================



EVERNOTE_AUTH_TOKEN=os.environ.get("EVERNOTE_AUTH_TOKEN")
if (EVERNOTE_AUTH_TOKEN == None):
    print('FATAL - env EVERNOTE_AUTH_TOKEN not defined - Exit service')
    quit()


EVERNOTE_PORT = os.environ.get("EVERNOTE_PORT")
if (EVERNOTE_PORT == None):
    EVERNOTE_PORT=EVERNOTE_PORT_DEFAULT




# ==========================
# Init of variables, etc.
# ==========================

APP = Flask(__name__,static_folder='public', static_url_path='')


def init():
    init_logger()
    init_evernote()


def init_evernote():
    global EVERNOTE
    sandbox=False
    china=False
    client = EvernoteClient(token=EVERNOTE_AUTH_TOKEN, sandbox=sandbox,china=china)
    user_store = client.get_user_store()
    EVERNOTE = client.get_note_store()


def init_logger():
    global LOGGER
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(console_handler)

    LOGGER = logger


