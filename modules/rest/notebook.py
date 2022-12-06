# from typing import Dict, List
from modules.evernote import notebook as evernote_notebook


def get_notebooks(request):
    notebooks = evernote_notebook.get_notebooks()
    result = { 'result' : 'ok', 'notebooks' : notebooks }
    return result

def get_notebooks(request):
    notebooks = evernote_notebook.get_notebooks()
    result = { 'result' : 'ok', 'notebooks' : notebooks }
    return result

def get_notes(request,notebook_guid):
    notes = evernote_notebook.get_notes(notebook_guid)
    result = { 'result' : 'ok','notes' : notes }
    return result
