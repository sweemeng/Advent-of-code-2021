from collections import defaultdict
import heapq
from itertools import product
import colorama as cr

def parse(path):
  data = {}
  with open(path) as f:
    row = 0
    length = 0
    for line in f:
      line = line.strip("\n")
      length = len(line)
      for i in range(length):
        data[(row, i)] = int(line[i])
      row += 1
  # return only row because this is a square
  return data, row


def walk_simple(data, size):
  # only exist for example
  # original implementation, never used
  seen = set()
  pos = (0, 0)
  scores = data[pos]
  print(data.keys())
  print(scores)
  while pos != (size-1, size-1):
    print(pos)
    seen.add(pos)
    row, col = pos
    adjuncts = get_adjucts(row, col, size, seen)
    
    lowest, score = lowest_score(adjuncts, data)
    scores += score
    pos = lowest
    print(score)
  scores += data[(size-1, size-1)]
  print(data[(size-1, size-1)])
  print("Total:",scores)


def dwalk(data, size):
  # implementation with list, a bit clearer. 
  # Mostly true'ish to pseudocode implementation of 
  # djikstra
  q = list(data.keys())
  dist = {k: 10000 for k in data}
  dist[(0,0)] = 0
  target = (size-1, size-1)
  prev = {}

  while len(q):
    md = min([dist[i] for i in q])
    us = [i for i in q if dist[i] == md]
    u = us[-1]
    if u == target:
      break
    q.remove(u)
    row, col = u
    neighbors = get_adjucts(row, col, size)
    for v in neighbors:
      if v in q:
        alt = md + data[v]
        if alt < dist[v]:
          dist[v] = alt
          prev[v] = u


  print(dist[(size-1,size-1)])
  print_data(data, size, prev)


# because this is not a full priority queue implementation
def dwalk_with_heap(data, size, print_mode=True):
  q = []
  visited = set()
  
  dist = defaultdict(lambda: 10000)
  dist[(0,0)] = 0
  for k,v in dist.items():
    heapq.heappush(q, (v, k))

  target = (size-1, size-1)
  prev = {}

  while len(q):
    md, u = heapq.heappop(q)

    if u == target:
      # the queue will not be empty ok, never will
      break
    visited.add(u)
    row, col = u
    neighbors = get_adjucts(row, col, size)
    for v in neighbors:
      if v in visited:
        continue
      alt = md + data.get(v)
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u
        heapq.heappush(q, (alt, v))


  print(dist[(size-1,size-1)])
  if print_mode:
    print_data(data, size, prev)
  

def lowest_score(adjuncts, data):
  scores = [data[i] for i in adjuncts]
  minimum = min(scores)
  for idx,value in enumerate(scores):
    if value == minimum:
      return adjuncts[idx], value
  return None


def get_adjucts(row, col, size, seen=None):
  # Do from bottom first then right, 
  adjuncts = [
    (row-1,col),(row, col-1),(row,col+1),(row+1, col),
  ]
  if seen:
    adjuncts = [i for i in adjuncts if i not in seen]
  adjuncts = [(row, col) for row, col in adjuncts if row >=0]
  adjuncts = [(row, col) for row, col in adjuncts if col >=0]
  adjuncts = [(row, col) for row, col in adjuncts if row <size]
  adjuncts = [(row, col) for row, col in adjuncts if col <size]
  return adjuncts


def print_data(data, size, path):
  p = (size-1, size-1)
  p_set = set()
  while p:
    p_set.add(p)
    p = path.get(p)

  for row,col in product(range(0,size), range(0,size)):
    if col == size-1:
      end = "\n"
    else:
      end = ""
    if (row,col) in p_set:
      
      print(f"{cr.Back.GREEN}{data.get((row,col))}",end="")
      print(cr.Style.RESET_ALL, end=end)
    else:
      print(data.get((row,col)), end=end)