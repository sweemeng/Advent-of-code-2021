from typing import Tuple, List


def h_test(p1: Tuple[int, int], p2: Tuple[int, int]) -> bool:
  x1, _ = p1
  x2, _ = p2
  return x1 == x2


def v_test(p1: Tuple[int, int], p2: Tuple[int, int]) -> bool:
  _, y1 = p1
  _, y2 = p2
  return y1 == y2

def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
  line = line.strip("\n")
  p1_str, p2_str = line.split(" -> ")
  tp1 = [int(i) for i in p1_str.split(",")]
  tp2 = [int(i) for i in p2_str.split(",")]
  return tuple(tp1), tuple(tp2)
  

def parse(path: str) -> List:
  results = []
  with open(path) as f:
    for i in f:
      temp = parse_line(i)
      results.append(temp)
  return results


def make_points(line):
  p1, p2 = line
  x1, y1 = p1
  x2, y2 = p2
  x = x1
  y = y1
  while x != x2 or y != y2:
    yield(x, y)
    if x > x2:
      x -= 1
    elif x < x2 :
      x +=1
    if y > y2:
      y -= 1
    elif y < y2:
      y += 1
  yield(x2, y2)
  