from collections import Counter
import copy


def parse(path):

  template = None
  rules = {}

  with open(path) as f:
    template = f.readline()
    template = template.strip("\n")
    f.readline()
    for line in f:
      line = line.strip("\n")
      t,o = line.split(" -> ")

      rules[(t[0], t[1])] = o
  return template, rules
      
def polymerize_step(sequence, rules):
  # Naive method, work but is too slow. 
  new_sequence = ""
  length = len(sequence)
  cache = {}
  for idx in range(length):
    c1 = sequence[idx]
    new_sequence += c1
    if idx + 1 == length:
      break
    
    c2 = sequence[idx+1]
    current = f"{c1}{c2}"
    if current in cache:
      pass
    mid = rules[(c1,c2)]
    new_sequence += mid
  
  return new_sequence

def count_subsequence(sequence):
  length = len(sequence)
  counter = Counter()
  for idx in range(length):
    if idx + 1 == length:
      # last item, Good bye
      break

    c1 = sequence[idx]
    c2 = sequence[idx+1]
    counter[(c1, c2)] += 1
  
  return counter

def polymerize(counter, rules):
  new_counter = Counter()
  # This only count new sequences. 
  for key in counter:
    c1, c2 = key
  
    mid = rules[key]
    # There is N amount of c1,c2 subsequence. They are expanded at the same time,
    # Don't worry worry about old sequence. Make new one
    new_counter[(c1, mid)] += counter[key]
    new_counter[(mid, c2)] += counter[key]
  
  return new_counter

