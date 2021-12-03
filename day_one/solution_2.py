def main():
  larger_count = 0
  buffer = []
  with open("day_one/input.txt") as f:
    prev = None
    for i in f:
      buffer.append(int(i))
      
      if len(buffer) > 3:
        buffer.pop(0)
      elif len(buffer) < 3:
        continue
      
      if prev:
        if sum(buffer) > prev:
          larger_count += 1
      prev = sum(buffer)
  print(larger_count)

  