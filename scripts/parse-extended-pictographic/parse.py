from __future__ import print_function
import codecs
import re
import sys

def main(input, output):
    code_point_re = re.compile(r'^U\+([0-9a-fA-F]+)\s*;\s*ExtendedPictographic.*$')
    code_point_range_re = re.compile(r'^U\+([0-9a-fA-F]+)\.\.U\+([0-9a-fA-F]+)\s*;\s*ExtendedPictographic.*$')

    for line in input:
        if m := code_point_re.match(line):
            print(f'set.add(0x{m[1]});', file=output)
        elif m := code_point_range_re.match(line):
            print(f'set.add(0x{m[1]}, 0x{m[2]});', file=output)

if __name__ == '__main__':
    with codecs.open(sys.argv[1], 'r', 'utf-8') as f:
        main(f, sys.stdout)
