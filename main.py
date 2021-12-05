import day_01.solution_1 as day_11
import day_01.solution_2 as day_12
import day_02.solution_1 as day_21
import day_02.solution_2 as day_22
import day_03.solution_1 as day_31
import day_03.solution_2 as day_32
import day_04.solution_1 as day_41
import day_04.solution_2 as day_42
import day_05.solution_1 as day_51
import day_05.solution_2 as day_52

def main():
  day = 5
  solution = 2
  if day == 1 and solution == 1:
    day_11.main()
  if day == 1 and solution == 2:
    day_12.main()
  if day == 2 and solution == 1:
    day_21.main()
  if day ==  2 and solution == 2:
    day_22.main()
  if day == 3 and solution == 1:
    day_31.solution("day_03/input.txt")
  if day == 3 and solution == 2:
    day_32.solution("day_03/input.txt")
  if day == 4 and solution == 1:
    day_41.solution("day_04/input.txt")
  if day == 4 and solution == 2:
    day_42.solution("day_04/input.txt")
  if day == 5 and solution == 1:
    day_51.solution("day_05/input.txt")
  if day == 5 and solution == 2:
    day_52.solution("day_05/input.txt")

if __name__ == "__main__":
  main()