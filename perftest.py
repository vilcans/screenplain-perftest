#!/usr/bin/env python

from tempfile import mkdtemp
import sys
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


if __name__ == '__main__':
    test_to_html()
    test_to_fdx()
    test_to_pdf()
