import config

def get_tags(filter=None):
  tags = config.EVERNOTE.listTags()
  result = {}
  for tag in tags:
    result[tag.guid] = {'guid':tag.guid,'name':tag.name,'parentGuid':tag.parentGuid}
  return result