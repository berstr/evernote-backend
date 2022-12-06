
import config

def health(request):
    result = { 'result' : 'ok', 'service' : 'evernote' }
    return result