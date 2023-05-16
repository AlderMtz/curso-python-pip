import random

def choose_options():
  options = ("piedra", "papel", "tijera") 
  user_option = input("piedra, papel o tijera=>\n")
  user_option = user_option.lower()
  
  if not user_option in options:
    print("Esa opcion no es valida\n")
    return None, None
    #continue 
  
  computer_option = random.choice(options)
  print("User option =>", user_option)
  print("Computer option =>", computer_option)
  return  user_option, computer_option  

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option and user_option != None:
    print("Empate")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Piedra gana a tijera")
      print("Usario ganó")
      user_wins += 1
    else:
      print("Papel gana a piedra")
      print("Computadora ganó")
      computer_wins += 1
      
  elif user_option == "papel":
    if computer_option == "piedra":
      print("Papel gana a piedra")
      print("Usario ganó")
      user_wins += 1
    else:
      print("Tijera gana a papel")
      print("Computadora ganó")
      computer_wins += 1

  elif user_option == "tijera":
    if computer_option == "papel":
      print("Tijera gana a papel")
      print("Usario ganó")
      user_wins += 1
    else:
      print("Piedra gana a tijera")
      print("Computadora ganó")
      computer_wins += 1
  return user_wins, computer_wins



def check_winner(user_wins, computer_wins):
  if user_wins == 2:
      print(f"\n Juego finalizado, usuario ganó {user_wins} veces")
      return True
  if computer_wins == 2:
      print(f"\n Juego finalizado, computadora ganó {computer_wins} veces")
      return True
  elif user_wins < 2 or computer_wins < 2:
    return False
  
  
def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  status = False
  while True:
    if not rounds == 1:
      print("\n")
    print("*" * 10)
    print(f"Round => {rounds}")
    print(f"Victorias de usuario => {user_wins}")
    print(f"Victorias de usuario => {computer_wins}")
    print("*" * 10)
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    rounds += 1
    status = check_winner(user_wins, computer_wins)
    if status == True:
      break
    
run_game()