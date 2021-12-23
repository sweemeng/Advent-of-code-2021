from day_14 import utils
from collections import Counter


def solution(path):
  sequence, rules = utils.parse(path)
  subsequences = utils.count_subsequence(sequence)
  
  for i in range(40):
    subsequences = utils.polymerize(subsequences, rules)
  
  counter = Counter()
  # because it is easier to count starting the second char, because if count first char it will overcount, due to overlap. Put in the first char first
  counter.update({sequence[0]: 1})
  for key in subsequences:
    c1, c2 = key
    value = subsequences[key]
    
    counter.update({c2: value})
  
  max_c = max(counter.values())
  min_c = min(counter.values())
  print(max_c)
  print(min_c)
  print(max_c - min_c)