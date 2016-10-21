#!/usr/bin/env python
import sys, re
from pprint import pprint

print "Multibind begin"

if int(sys.argv[1]) & 1:
    sys.path.insert(0, './group_a/cythlib')
    import cynative as cynative_a

    oldmod = dict(sys.modules)
    for k in oldmod:
        if re.match(r'cynative(\.|$)', k):
            newk = k.replace('cynative', 'cynative_a', 1)
            sys.modules[newk] = sys.modules[k]
            # The following may or may not be a good idea
            #sys.modules[newk].__name__ = newk
            del sys.modules[k]
    sys.path.pop(0)
    
if int(sys.argv[1]) & 2:
    sys.path.insert(0, './group_b/cythlib')
    import cynative as cynative_b
    oldmod = dict(sys.modules)
    for k in oldmod:
        if re.match(r'cynative(\.|$)', k):
            newk = k.replace('cynative', 'cynative_b', 1)
            sys.modules[newk] = sys.modules[k]
            # The following may or may not be a good idea
            #sys.modules[newk].__name__ = newk
            del sys.modules[k]
    sys.path.pop(0)

if int(sys.argv[1]) & 1:
    print "Cynative A"
    cynative_a.cyprint_version()
    cynative_a.cyprint_native_version()
    print

if int(sys.argv[1]) & 2:
    print "Cynative B"
    cynative_b.cyprint_version()
    cynative_b.cyprint_native_version()
    print

print "Multibind end"
