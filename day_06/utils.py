from collections import Counter

def parse(path: str) -> Counter:
  f=open(path)
  data_str = f.read()
  data_str = data_str.strip("\n")
  data = [int(i) for i in data_str.split(',')]
  counter = Counter(data)
  return counter

def aquarium(path, days):
  counter = parse(path)
  for i in range(days):
    num_mama = counter[0]
    num_baby = num_mama
    # Clean up first
    next_cycle = Counter()
    next_cycle.update({6: num_mama})
    next_cycle.update({8: num_baby})
    for timer in range(1,9):
      next_timer = timer - 1
      next_cycle.update({next_timer: counter[timer]})
    for timer in next_cycle:
      counter[timer] = next_cycle[timer]
  print(sum(counter.values()))