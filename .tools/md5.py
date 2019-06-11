#!/usr/bin/env python
import hashlib
import sys
 
def md5(s):
    return hashlib.md5(s).hexdigest()
 
for i in range(1, 9999999):
    if md5(str(i)).startswith(sys.argv[1]):
    	print(i)
    	break
