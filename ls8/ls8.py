#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

#if len(sys.argv) != 2:
#    print("Incorrect number of arguments passed in")
#else:
cpu = CPU()
cpu.load()
cpu.run()