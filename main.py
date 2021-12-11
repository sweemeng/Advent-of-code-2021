from solutions import *

def main():
  day = 11
  solution = 2
  test_mode = False
  day_path = "day_11"
  
  if test_mode:
    file_name = "test"
  else:
    file_name = "input"
  path = f"{day_path}/{file_name}.txt"
  if day == 1 and solution == 1:
    day_11.main()
  if day == 1 and solution == 2:
    day_12.main()
  if day == 2 and solution == 1:
    day_21.main()
  if day ==  2 and solution == 2:
    day_22.main()
  if day == 3 and solution == 1:
    day_31.solution(path)
  if day == 3 and solution == 2:
    day_32.solution(path)
  if day == 4 and solution == 1:
    day_41.solution(path)
  if day == 4 and solution == 2:
    day_42.solution(path)
  if day == 5 and solution == 1:
    day_51.solution(path)
  if day == 5 and solution == 2:
    day_52.solution(path)
  if day == 6 and solution == 1:
    day_61.solution(path)
  if day == 6 and solution == 2:
    day_62.solution(path)
  if day == 7 and solution == 1:
    day_71.solution(path)
  if day == 7 and solution == 2:
    day_72.solution(path)
  if day == 8 and solution == 1:
    day_81.solution(path)
  if day == 8 and solution == 2:
    day_82.solution(path)
  if day == 9 and solution == 1:
    day_91.solution(path)
  if day == 9 and solution == 2:
    day_92.solution(path)
  if day == 10 and solution == 1:
    day_101.solution(path)
  if day == 10 and solution == 2:
    day_102.solution(path)
  if day == 11 and solution == 1:
    day_111.solution(path)
  if day == 11 and solution == 2:
    day_112.solution(path)

if __name__ == "__main__":
  main()