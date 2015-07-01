#!/usr/bin/env python

from tempfile import mkdtemp
import json
import sys
from time import time
sys.path.append('screenplain/')
from screenplain.main import main

filename = 'input/Big-Fish.fountain'

outfile = '/tmp/loadimpactresults.json'

out_dir = mkdtemp()


def test_to_html():
    main([filename, out_dir + '/out.html'])


def test_to_fdx():
    main([filename, out_dir + '/out.fdx'])


def test_to_pdf():
    main([filename, out_dir + '/out.pdf'])


def measure_all():
    funcs = [test_to_html, test_to_fdx, test_to_pdf]
    results = {f.__name__: measure(f) for f in funcs}
    output(results)


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


def output(results):
    json_results = [{'name': n, 'value': s} for n, s in results.items() if s is not None]
    assert json_results  # If we have no results at all, that's a fail.
    with open(outfile, 'w') as f:
        json.dump({'results': json_results}, f, indent=4)


if __name__ == '__main__':
    measure_all()
