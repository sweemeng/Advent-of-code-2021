from day_14 import utils
from collections import Counter


def solution(path):
  sequence, rules = utils.parse(path)
  print(sequence)
  subsequences = utils.count_subsequence(sequence)
  print()
  print(subsequences)
  for i in range(10):
    print(i)
    subsequences = utils.polymerize(subsequences, rules)
    print(subsequences)
  
  counter = Counter()
  for key in subsequences:
    c1, c2 = key
    value = subsequences[key]
    #counter.update({c1: value})
    counter.update({c2: value})
  
  max_c = max(counter.values())
  min_c = min(counter.values())
  print(max_c)
  print(min_c)
  print(max_c - min_c)