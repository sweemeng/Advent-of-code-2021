from day_10 import utils

def solution(path: str):
  with open(path) as f:
    
    score = 0
    for line in f:
      stack = []
      for c in line:
        if not stack:
          stack.append(c)
          continue
        if c in utils.close_tokens:
          test_c = utils.close_tokens[c]
          to_close = stack[-1]
          if test_c == to_close:
            stack.pop()
          else:
            score += utils.close_token_score[c]
            break
        else:
          stack.append(c)
    print(score)
          