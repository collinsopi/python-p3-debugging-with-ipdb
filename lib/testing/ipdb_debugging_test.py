#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from lib.ipdb_debugging import plus_two

class TestIpdbDebugging:
    '''ipdb_debugging.py'''
    
    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum.'''
        assert(plus_two(3) == 5)
