#!/usr/bin/env python

import zipfile
import sys

#Set search parameters
creator = '<dc:creator>'
createEnd = '</dc:creator>'

modifiedBy = '<cp:lastModifiedBy>'
modifiedByEnd = '</cp:lastModifiedBy>'

revision = '<cp:revision>'
revisionEnd = '<cp:revision>'

createdDate = '<dcterms:created'
createdDateEnd = '</dcterms:created>'

modified = '<dcterms:modified'
modifiedEnd = '</dcterms:modified>'

lastPrinted = '<cp:lastPrinted>'
lastPrintedEnd = '</cp:lastPrinted>'

#zf = zipfile.ZipFile('/Users/Gerry/Desktop/test.docx')
zf = zipfile.ZipFile(sys.argv[1])
meta = zf.read('docProps/core.xml')

#Need to search the string for creator and last modified etc.
print 'Author: %s' % meta[meta.find(creator)+len(creator):meta.find(createEnd)]
#Below can be made more siple in terms of searching from the end for date.
print 'Last modified by %s on %s' % (meta[meta.find(modifiedBy)+len(modifiedBy):meta.find(modifiedByEnd)],
                                     meta[meta.find(modifiedEnd)-20:meta.find(modifiedEnd)])

print 'File created on : %s' % meta[meta.find(createdDateEnd)-20:meta.find(createdDateEnd)-1]
print 'Last printed: %s' % meta[meta.find(lastPrintedEnd)-20:meta.find(lastPrintedEnd)-1]
