#!/usr/bin/env python

# 1. Load the input to memory

import sys

digits = '123456789'

def pretty_print(values):
  width = max(len(s) for s in values.values())
  for row in range(9):
    for col in range(9):
      sys.stdout.write(values[(row, col)].center(width))
      if col != 8:
        sys.stdout.write(' ')
      if col in [2, 5]:
        sys.stdout.write('| ')
    sys.stdout.write('\n')
    if row in [2, 5]:
      sys.stdout.write('-+-'.join(['-'.join(['-' * width] * 3)] * 3))
      sys.stdout.write('\n')


def parse_grid(grid):
  values = {}
  i = 0
  for c in grid:
    if c in digits:
      values[(i/9, i%9)] = c
      i += 1
    elif c in '0.':
      values[(i/9, i%9)] = digits
      i += 1
  if i != 81:
    return False
  return values

if __name__ == '__main__':
  pretty_print(parse_grid(open(sys.argv[1]).read()))
