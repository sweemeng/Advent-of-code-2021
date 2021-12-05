from day_05 import utils
from collections import Counter

def solution(path: str):
  lines = utils.parse(path)
  
  maps = set()
  counter = Counter()
  for line in lines:
    for point in utils.make_points(line):
      if point in maps:
        counter.update({point: 1})
      else:
        maps.add(point)
  
  print(len(counter))