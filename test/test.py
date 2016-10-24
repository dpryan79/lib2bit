#!/usr/bin/env python
"""
The expected output is below:

0	chr1	150 offset 0x4a
1	chr2	100 offset 0x88
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNACGTACGTACGTagctagctGATCGATCGTAGCTAGCTAGCTAGCTGATCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNACGTACGTACGTagctagctGATC
0	0.086667
1	0.080000
2	0.080000
3	0.086667
0	0.120000
1	0.120000
2	0.120000
3	0.120000
"""
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
assert(md5sum == "55e28106e51c37e9191846f0b69a7b52")

print("Passed!")
