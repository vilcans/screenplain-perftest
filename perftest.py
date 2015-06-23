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
    function()
    seconds = time() - start
    print function.__name__, seconds
    return seconds


def output(results):
    json_results = [format_result(name, seconds) for name, seconds in results.items()]
    with open(outfile, 'w') as f:
        json.dump({'results': json_results}, f, indent=4)


def format_result(name, s):
    aggregates = {'latency': {'avg': s, 'p90': s, 'p99': s} }
    return {'name': name,
            'aggregates': aggregates}


if __name__ == '__main__':
    measure_all()
