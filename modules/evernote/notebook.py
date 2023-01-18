from evernote.edam.notestore.ttypes import NoteFilter, NoteList

import config

def get_notebooks(filter=None):
  notebooks = config.EVERNOTE.listNotebooks()
  # print("Found ", len(notebooks), " notebooks:")
  result = []
  for notebook in notebooks:
    result.append({'name': notebook.name, 'guid' : notebook.guid, 'stack':notebook.stack})
  return result


def get_notes(notebook_guid):
  filter = NoteFilter(notebookGuid = notebook_guid)

  startIndex = 0
  get_notes_count = 100
  result = []
  while True:
    notes = config.EVERNOTE.findNotes(filter,startIndex,get_notes_count)
    config.LOGGER.info(f'notebook:get_notes() - total notes: {notes.totalNotes} -  number of notes: {len(notes.notes)} - max notes per request: {get_notes_count}')

    i = startIndex + 1
    for note in notes.notes:
      result.append({ 'title':note.title, 'guid':note.guid, 'tagGuids':note.tagGuids, 'notebookGuid':note.notebookGuid})
      config.LOGGER.info(f'notebook:get_notes() - [{i}] title: {note.title}')
      i = i + 1

    startIndex = startIndex + len(notes.notes)
    if startIndex >= notes.totalNotes:
      break
  return result

def get_note(note_guid):
  return config.EVERNOTE.getNote(note_guid, True, False, False, False)

'''
  do {
    filter.setNotebookGuid(notebook_guid);
	  notes = config.EVERNOTE.findNotesMetadata(config.EVERNOTE.EVERNOTE_AUTH_TOKEN, filter, offset, pageSize, spec);
	  for (NoteMetadata note : notes.getNotes() {
      print(note.title)
	  }
	  offset = offset + notes.getNotesSize();
  } while (notes.getTotalNotes() > offset);
'''
