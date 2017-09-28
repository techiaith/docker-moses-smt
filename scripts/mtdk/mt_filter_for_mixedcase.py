#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
 
file=str(sys.argv[1])

with open (file) as f:
	for line in f:
		sline=line.strip()
		if not sline.islower():
			if not sline.isdigit():
				if len(sline) > 1:
					if sline[0].isupper():
						print sline

