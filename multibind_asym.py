#!/usr/bin/env python
import sys, re

print "Multibind asym begin"
print
import cynative

print "'Official' cynative after NORMAL import:"
cynative.cyprint_version()
cynative.cyprint_native_version()
print

cynative_gem = None

def load_custom_module():
    global cynative_gem

    # change the name of the "official" module to avoid caching during import
    oldmod = dict(sys.modules)
    for k in oldmod:
        if re.match(r'cynative(\.|$)', k):
            newk = k.replace('cynative', 'cynative_gem_off', 1)
            sys.modules[newk] = sys.modules[k]
            # The following may or may not be a good idea
            #sys.modules[newk].__name__ = newk
            del sys.modules[k]

    # import the custom module
    sys.path.insert(0, './group_b/cythlib')
    import cynative as cynative_gem
    oldmod = dict(sys.modules)
    for k in oldmod:
        if re.match(r'cynative(\.|$)', k):
            newk = k.replace('cynative', 'cynative_gem', 1)
            sys.modules[newk] = sys.modules[k]
            # The following may or may not be a good idea
            #sys.modules[newk].__name__ = newk
            del sys.modules[k]
    sys.path.pop(0)

    # revert the "official" version name
    oldmod = dict(sys.modules)
    for k in oldmod:
        if re.match(r'cynative(\.|$)', k):
            newk = k.replace('cynative_gem_off', 'cynative', 1)
            sys.modules[newk] = sys.modules[k]
            # The following may or may not be a good idea
            #sys.modules[newk].__name__ = newk
            del sys.modules[k]


#
#  MAIN
#

load_custom_module()

print "'Official' cynative after CUSTOM import:"
cynative.cyprint_version()
cynative.cyprint_native_version()
print

print "'Custom' cynative after CUSTOM import:"
cynative_gem.cyprint_version()
cynative_gem.cyprint_native_version()
print

print "Multibind asym end"
