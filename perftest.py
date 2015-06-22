#!/usr/bin/env python

from tempfile import mkdtemp
import sys
from time import time
sys.path.append('screenplain/')
from screenplain.main import main

filename = 'input/Big-Fish.fountain'

out_dir = mkdtemp()


def test_to_html():
    main([filename, out_dir + '/out.html'])


def test_to_fdx():
    main([filename, out_dir + '/out.fdx'])


def test_to_pdf():
    main([filename, out_dir + '/out.pdf'])


def measure(function):
    start = time()
    function()
    seconds = time() - start
    print function.__name__, seconds

if __name__ == '__main__':
    measure(test_to_html)
    measure(test_to_fdx)
    measure(test_to_pdf)
