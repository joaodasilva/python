#!/usr/bin/env python

# 1. Load the input to memory

import sys

digits = '123456789'
indices = [(row, col) for row in range(9) for col in range(9)]

def group(iterable, times):
  return zip(*[iter(iterable)] * times)

def pretty_print(values):
  width = max(len(s) for s in values.values())
  items = [values[(row, col)].center(width) for row, col in indices ]
  rows = [' '.join(l) for l in group(items, 3)]
  grid = [' | '.join(s) for s in group(rows, 3)]
  sep = '\n' + '-+-'.join(['-'.join(['-' * width] * 3)] * 3) + '\n'
  print sep.join(['\n'.join(l) for l in group(grid, 3)])

def parse_grid(grid):
  return dict(zip(indices, (c if c in digits else digits
                            for c in grid if c in digits or c in '0.')))

if __name__ == '__main__':
  pretty_print(parse_grid(open(sys.argv[1]).read()))
