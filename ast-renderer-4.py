
import mistune
import pprint
from pylatex import (
  Document, Section, Subsection, Command)
from pylatex.utils import italic, NoEscape


markdown = mistune.create_markdown ( 
  renderer=mistune.AstRenderer ())

f = open ('example-1.md')
content = f.read ()
f.close ()

""" example-5.md:
# Header One

## Subheader One

Text one.

## Subheader Two

Text two.
"""    

pp = pprint.PrettyPrinter (width=65)
pp.pprint (content)

""" prints:
('# Header One\n'
 '\n'
 '## Subheader One\n'
 '\n'
 'Text one.\n'
 '\n'
 '## Subheader Two\n'
 '\n'
 'Text two.\n'
 '\n')
"""

md = markdown (content)

pp.pprint (md)

""" prints:
[{'children': [{'text': 'Header One', 'type': 'text'}],
  'level': 1,
  'type': 'heading'},
 {'children': [{'text': 'Subheader One', 'type': 'text'}],
  'level': 2,
  'type': 'heading'},
 {'children': [{'text': 'Text one.', 'type': 'text'}],
  'type': 'paragraph'},
 {'children': [{'text': 'Subheader Two', 'type': 'text'}],
  'level': 2,
  'type': 'heading'},
 {'children': [{'text': 'Text two.', 'type': 'text'}],
  'type': 'paragraph'}]
"""

def node2 (m):
  result = ""
  if m ['type'] == 'text':
    result = m ['text']
  return result

def loop2 (children):
  result = ""
  for m in children:
    result += node2 (m)
  return result

def node1 (m):
  result = ""
  if m ['type'] == 'heading':
    if m ['level'] == 1:
      result = Section (loop2 (m ['children']))
    if m ['level'] == 2:
      result = Subsection (loop2 (m ['children']))
  if m ['type'] == 'paragraph':
    result = loop2 (m ['children'])
  return result

doc = Document ("example-1")


for m in md:
  doc.append (node1 (m))

doc.generate_pdf (clean_tex=False)


