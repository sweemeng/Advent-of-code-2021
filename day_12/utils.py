from typing import List, Dict, Tuple
import copy
from collections import Counter
from functools import lru_cache


class PathMaps:
  def __init__(self):
    self.a_tables: Dict[str,List[str]] = {
      "start":[]
    }
    self.connections: List[Tuple[str, str]] = []
    self.paths = []
    self.small_cave = set(['start'])

  def parse(self, path):
    with open(path) as f:
      for line in f:
        line = line.strip("\n")
        node_1, node_2 = line.split("-")
        if node_1[0].islower() and node_1 not in ['start','end']:
          self.small_cave.add(node_1)
        if node_2[0].islower() and node_1 not in ['start','end']:
          self.small_cave.add(node_2)
        if node_1 != "end":
          if node_2 != "start":
            self.connections.append((node_1, node_2))
        if node_1 != "start":
          if node_2 != "end":
              self.connections.append((node_2, node_1))

  def build_tables(self):
    for path in self.connections:
      node_1, node_2 = path
      conn_1 = self.a_tables.setdefault(node_1, [])
      if node_2 not in conn_1:
        conn_1.append(node_2)

  def walk(self, node="start", small_visit_time=1):
    
    s = set()
    stack = []
    stack.insert(0, node)
    # i can use tuple, whatevs. if not set exist, i use a dict as a trie
    s.add(str(stack))
    count = 0
    while True:
      check = node
      node = None
      for option in self.a_tables[check]:
        if small_visit_time == 2:
          invalid = self.cant_insert_two_visit(stack, option)
        else:
          invalid = self.cant_insert_simple(stack, option)
        if invalid:
          continue
        stack.insert(0, option)
        if str(stack) in s:
          # we seen this before
          stack.pop(0)
          continue
        node = option
        s.add(str(stack))
        break
      if not node:
        stack.pop(0)
        if stack:
          node = stack[0]
      if node == 'end':
        count += 1
        s.add(str(stack))
        stack.pop(0)
        if stack:
          node = stack[0]
        

      if not stack:
        # happen when we pop start, so please put this at the end
        break  
    print(count)
  
  def cant_insert_two_visit(self, stack, node):
    if node not in self.small_cave:
      return False
    c = Counter(stack)
  
    visited_twice = None
    for key in c:
      if key in self.small_cave:
          if c[key] >= 2:
            visited_twice = key
            break
    
    if visited_twice:
      if node in stack:
        return True
    
    return False

  def cant_insert_simple(self, stack, node):
    if node in self.small_cave:
      if node in stack:
        return True
    return False

