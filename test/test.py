#!/usr/bin/env python
from subprocess import Popen, PIPE, check_call
from os import remove

# N.B., this MUST be run from within the source directory!

# Read test
p1 = Popen(["./test/exampleRead", "test/foo.2bit"], stdout=PIPE)
try:
    p2 = Popen(["md5sum"], stdin=p1.stdout, stdout=PIPE)
except:
    p2 = Popen(["md5"], stdin=p1.stdout, stdout=PIPE)
md5sum = p2.communicate()[0].strip().split()[0]
assert(md5sum == "0274c32c7f3dd75e8991f6107dca6a5f")

print("Passed!")
