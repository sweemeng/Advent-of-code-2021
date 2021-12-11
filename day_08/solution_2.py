from day_08 import utils


def segmentation(signals):
  # group by length 
  group = {}
  for signal in signals:
    l = len(signal)
    segment = group.get(l, [])
    segment.append(signal)
    group[l] = segment
  return group

# lookup table is dict so pass by reference
def simple_solve(segments, reverse_lookup):
  # Simple size i will just hard code
  one = segments[2][0]
  reverse_lookup[1] = one
  seven = segments[3][0]
  reverse_lookup[7] = seven
  four = segments[4][0]
  reverse_lookup[4] = four
  eight = segments[7][0]
  reverse_lookup[8] = eight

def solve_for(
  segments, 
  reverse_lookup,
  segment_size,
  target,
  embedded_segment,
):
  candidates = segments[segment_size]
  embedded = reverse_lookup[embedded_segment]
  for item in candidates:
    sub = set(embedded)
    sup = set(item)
    # We alread solve this
    if item in reverse_lookup.values():
      continue
    if sub.issubset(sup):
      reverse_lookup[target] = item

def solve_remainder(segments, reverse_lookup):
  # We already solve 0, 9, only 6 remains in 6 segments
  segment_6 = [segment for segment in segments[6] if segment not in reverse_lookup.values()]
  six = segment_6[0]
  reverse_lookup[6] = six
  # only 2,5
  segments_5 = [segment for segment in segments[5] if segment not in reverse_lookup.values()]
  sub = set(segments_5[0])
  sup = set(six)
  # Only digit 5 is within 6 in the 7 segments
  if sub.issubset(sup):
    five = segments_5[0]
    two = segments_5[1]
  else:
    five = segments_5[1]
    two = segments_5[0]
  reverse_lookup[2] = two
  reverse_lookup[5] = five


def solve_digit(digit, reverse_lookup):
  for num,segment in reverse_lookup.items():
    if set(digit) == set(segment):
      return num


def solve_digits(digits, reverse_lookup):
  places = [1000, 100, 10, 1]
  p = 0
  answer = 0
  for digit in digits:
    temp = solve_digit(digit, reverse_lookup)
    answer += temp * places[p]
    p += 1
  return answer


def solution(path: str):
  results = []
  for signals, digits in utils.parse(path):
    reverse_lookup = {}
    segments = segmentation(signals)
    # This is known size so i will hard code
    simple_solve(segments, reverse_lookup)
    # Solve for 3
    # 3 need 5 segment in display, so length 5
    # 5 segment only have 2,3,5, one 3 have 1 embedded
    solve_for(segments, reverse_lookup,5, 3, 1)
    # 9 need 6 to display 
    # 6 segments have 0, 6, 9
    # 9 have segments of 3 in iter
    # We have solved 3
    solve_for(segments, reverse_lookup,6, 9, 3)
    # 9 is found, now we can search for zero, 
    # 1 is embedded in 0, but not 6 in the 6 segments
    solve_for(segments, reverse_lookup,6, 0, 1)
    # Now we can manually search 2,5,6
    solve_remainder(segments, reverse_lookup)
    num = solve_digits(digits, reverse_lookup)
    print(num)
    results.append(num)
  print(sum(results))
    







  