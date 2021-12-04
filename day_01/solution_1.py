def main():
  larger_count = 0
  with open("day_01/input.txt") as f:
    prev = None
    for i in f:
      if prev:
        if int(i) > prev:
          larger_count += 1
      prev = int(i)
  print(larger_count)

  