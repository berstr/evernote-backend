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
  get_notes_count = 4
  result = []
  while True:
    notes = config.EVERNOTE.findNotes(filter,startIndex,get_notes_count)

    for note in notes.notes:
      result.append({ 'title':note.title, 'guid':note.guid, 'tags':note.tagGuids, 'notebookGuid':note.notebookGuid})
      print(note.title)
      print(note)
      print('-----------------')
      if note.title == 'n4':
        c = config.EVERNOTE.getNote(note.guid, True, False, False, False)
        print('.....................')
        print(c)
      print('-----------------')
    startIndex = startIndex + len(notes.notes)
    # print('notes.totalNotes: ', notes.totalNotes)
    # print('startIndex: ',startIndex)
    # print('len(notes.notes): ',len(notes.notes))
    if startIndex >= notes.totalNotes:
      break
  # print(x.startIndex)  
  # print(x.totalNotes)
  # print(len(x.notes))  

  return result

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
