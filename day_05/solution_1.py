from day_05 import utils
from collections import Counter

def solution(path: str):
  lines = utils.parse(path)
  filtered = []
  for item in lines:
    p1, p2 = item 
    if utils.h_test(p1, p2):
      filtered.append(item)
      continue
    if utils.v_test(p1, p2):
      filtered.append(item)
      continue
  maps = set()
  counter = Counter()
  for line in filtered:
    for point in utils.make_points(line):
      if point in maps:
        counter.update({point: 1})
      else:
        maps.add(point)
  
  print(len(counter))