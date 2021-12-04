from day_four import utils

def solution(path: str):
  game_input, boards = utils.parse(path)
  players: utils.Player = []
  for board in boards:
    player = utils.Player(board)
    players.append(player)
  
  bingo = False

  for i in game_input:
    for player_id in range(len(players)):
      player = players[player_id]
      player.check(i)
      if player.bingo:
        bingo = True
        print(player.last_number)
        print(player_id)
        print(player.print_result())
    if bingo:
      break

      
  