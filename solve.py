#!/usr/bin/env python

import sys

digits = '123456789'
indices = [(row, col) for row in range(9) for col in range(9)]

def group(iterable, times):
  return zip(*[iter(iterable)] * times)

def assign(values, index, value):
  values[index] = value
  return True

def parse_grid(grid):
  values = dict((s, digits) for s in indices)
  grid = dict(zip(indices, (c for c in grid if c in digits or c in '0.')))
  assert len(grid) == 81
  if not all(assign(values, s, d) for s, d in grid.items() if d in digits):
    return False
  return values

def pretty_print(values):
  width = max(len(s) for s in values.values())
  items = [values[(row, col)].center(width) for row, col in indices ]
  rows = [' '.join(l) for l in group(items, 3)]
  grid = [' | '.join(s) for s in group(rows, 3)]
  sep = '\n' + '-+-'.join(['-'.join(['-' * width] * 3)] * 3) + '\n'
  print sep.join(['\n'.join(l) for l in group(grid, 3)])

if __name__ == '__main__':
  pretty_print(parse_grid(open(sys.argv[1]).read()))
