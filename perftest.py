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


def run():
    funcs = [test_to_html, test_to_fdx, test_to_pdf]
    results = {f.__name__: measure(f) for f in funcs}
    return results


def measure(function):
    start = time()
    try:
        function()
    except (Exception, SystemExit) as e:
        print e
        return None
    seconds = time() - start
    print function.__name__, seconds
    return seconds


if __name__ == '__main__':
    run()
