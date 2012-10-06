#!/usr/bin/env python

from copy import deepcopy
from itertools import *
import sys

def group(iterable, times):
  return zip(*[iter(iterable)] * times)

digits = '123456789'
indices = [(row, col) for row in range(9) for col in range(9)]

unitlist = ( group(indices, 9) +                        # rows
             group([(y, x) for x, y in indices], 9) +   # columns
             # squares
             [ tuple(product(rows, cols)) for rows in group(range(9), 3)
                                          for cols in group(range(9), 3) ] )

units = dict((s, filter(lambda unit: s in unit, unitlist)) for s in indices)

peers = dict((s, set(x for u in units[s] for x in u if x!=s)) for s in indices)

def remove(values, index, value):
  if value not in values[index]:
    # Already removed. Prevent infinite recursion between 2 slots with one
    # value each.
    return True
  values[index] = values[index].replace(value, '')
  if len(values[index]) == 0:
    # Removed all values.
    return False
  elif len(values[index]) == 1:
    # Single value: remove it from the peers of |index|.
    if not all(remove(values, p, values[index]) for p in peers[index]):
      return False
  # If a unit has only one slot left for |value|, put it there.
  for unit in units[index]:
    choices = [index for index in unit if value in values[index]]
    if len(choices) == 0:
      # No place for |value| available.
      return False
    elif len(choices) == 1 and not assign(values, choices[0], value):
      return False
  return True

def assign(values, index, value):
  # Invalid if any peer of |index| already has |value|.
  return all(remove(values, index, o) for o in values[index].replace(value, ''))

def parse_grid(grid):
  values = dict((s, digits) for s in indices)
  grid = dict(zip(indices, (c for c in grid if c in digits or c in '0.')))
  assert len(grid) == 81
  if not all(assign(values, s, d) for s, d in grid.items() if d in digits):
    return False
  return values

def search(values):
  choices = [(len(values[s]), s) for s in indices]
  if all(l == 1 for l, _ in choices):
    return values
  _, index = min((l, index) for l, index in choices if l > 1)
  for v in values[index]:
    copy = deepcopy(values)
    if assign(copy, index, v):
      result = search(copy)
      if result: return result
  return False

def solve(puzzle):
  values = parse_grid(puzzle)
  if not values:
    return False
  return search(values)

def pretty_print(values):
  width = max(len(s) for s in values.values())
  items = [values[(row, col)].center(width) for row, col in indices ]
  rows = [' '.join(l) for l in group(items, 3)]
  grid = [' | '.join(s) for s in group(rows, 3)]
  sep = '\n' + '-+-'.join(['-'.join(['-' * width] * 3)] * 3) + '\n'
  print sep.join(['\n'.join(l) for l in group(grid, 3)])

if __name__ == '__main__' and len(sys.argv) == 2:
  values = solve(open(sys.argv[1]).read())
  if values:
    pretty_print(values)
  else:
    print 'Error!'
