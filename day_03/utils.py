from typing import Callable, Dict, List


def assemble_bytes(data: Dict[int, dict], func: Callable):
  result_str = ""
  for pos in data:
    temp = func(data[pos], key=data[pos].get)
    result_str += temp
  
  return int(result_str, 2)


def count_bytes(data: List[str]):
  counter = {}
  for item in data:
      for pos in range(len(item)):
        curr = counter.get(pos, {"0":0, "1": 0})
        if item[pos] in ("0", "1"):
          curr[item[pos]] += 1
          counter[pos] = curr
  return counter
