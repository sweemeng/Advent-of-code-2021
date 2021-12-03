import day_one.solution_1 as day_11
import day_one.solution_2 as day_12
import day_two.solution_1 as day_21
import day_two.solution_2 as day_22
import day_three.solution_1 as day_31
import day_three.solution_2 as day_32

def main():
  day = 3
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
    day_31.solution("day_three/input.txt")
  if day == 3 and solution == 2:
    day_32.solution("day_three/input.txt")

if __name__ == "__main__":
  main()