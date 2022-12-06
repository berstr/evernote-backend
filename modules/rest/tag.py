# from typing import Dict, List
from modules.evernote import tag as evernote_tag


def get_tags(request):
    tags = evernote_tag.get_tags()
    result = { 'result' : 'ok', 'tags' : tags }
    return result
