import sys

PY2 = sys.version_info[0] == 2

if PY2:
    def iteritems(x):
        return x.iteritems()
else:
    def iteritems(x):
        return x.items()
