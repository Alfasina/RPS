import random





def game(a, b):
  print('User selected:', b, ' Computer selected:',a);
  if a==b:
      print ('its a Tie')
  elif a == 'R':
    if b =='S':
      print("You won! Rock crushes Scissors")
    else:
      print('Computer Wins! Paper covers Rock')
  elif a == 'P':
    if b =='R':
      print("You Won! Paper covers Rock")
    else:
      print('Computer wins! Scissors cut Paper')

  elif a == 'S':
    if b =='P':
      print("You Won! Scissors cut Paper")
    else:
      print('Computer Win! Rock crushes Scissors')
  else:
    print('Your Input is Invalid')

def repeat():
  
  i=0
  c=3
  while i < c:
    select= input('please type an option: R, P or S')
    outcome=["R","P","S"]
    computer=random.choice(outcome)
    game(select, computer)
    i+=1

repeat()