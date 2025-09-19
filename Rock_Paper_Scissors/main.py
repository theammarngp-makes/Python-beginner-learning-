import random 

emojis ={'r':' 🪨 ', 'p':'📜','s' :'✂️'}
choices =(tuple(emojis.keys()))

def get_choice():
    while True :
           player_choice = input('Rock , paper or scissors ?(r,p,s):').lower()
  
           if player_choice  in choices :
              return player_choice
           else : 
              print('INVALID ')   


                                                    
def play_choices( player_choice, computer_choice) :                                           
    print(f'You selceted: {emojis[player_choice]}')                 
    print(f'Computer selected :{emojis[computer_choice]}')   
                      
           
def winner(player_choice,computer_choice):
       
   if player_choice == computer_choice :
      print('Tie !')
 
   elif(
    (computer_choice=='s' and  player_choice  == 'r') or 
   (computer_choice=='p' and  player_choice  == 's') or 
   (computer_choice=='r' and   player_choice  == 'p') ) :
      print('You Win !')
      
   else :
       print('You lose ')                                                                                                         
def play_game() :                                                                                                                    
    while True :
        player_choice =get_choice()    
        computer_choice =random.choice(choices)                        
        play_choices(player_choice,computer_choice)
        winner(player_choice,computer_choice) 
    
  
        decision = input('Continue ? (Y/N):') 
        if decision =='y' :
            print('continue')
        elif decision != 'y'  :
            print('Invalid input , game ending...')
            break
            
play_game()          