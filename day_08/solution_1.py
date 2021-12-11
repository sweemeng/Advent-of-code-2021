from day_08 import utils


def solution(path: str):
  count = 0
  for signals, digits in utils.parse(path):
    for segment in digits:
      l = len(segment)
      if l in [2, 3, 4, 7]:
        count += 1
  print(count)