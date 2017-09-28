#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
 
file=str(sys.argv[1])
file2=str(sys.argv[2])

outfile=open(file2,'w')

with open (file) as f:
	for line in f:
		if line.startswith('PhraseDictionaryMemory'):
			line = line.replace('PhraseDictionaryMemory','PhraseDictionaryCompact')
			line = line.replace('table.gz','table.minphr') 
		if line.startswith('LexicalReordering'):
			line = line.replace('bidirectional-fe.gz','bidirectional-fe')

		outfile.write(line) 	

outfile.close()
