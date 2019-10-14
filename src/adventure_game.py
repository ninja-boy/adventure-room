#PYTHON PROGRAM TO CREATE AN ADVENTURE GAME

import random
def msg(room):
    if room['msg']=='':
        return "You have entered the "+ room['name'] +"."
    else:
        return room['msg']
def get_choice(room,dir):
    if dir=='N':
        choice=0
    elif dir=='E':
        choice=1
    elif dir=='S':
        choice=2
    elif dir=='W':
        choice=3
    else:
        return -1

    if room['directions'][choice]==0:
        return 4
    else:
        return choice

def main():
    dirs=(0,0,0,0)
    entrance={'name':'Entrance','directions':dirs,'msg':''}
    livingroom={'name':'Living Room','directions':dirs,'msg':''}
    corridor={'name':'Corridor','directions':dirs,'msg':''}
    kitchen={'name':'Kitchen','directions':dirs,'msg':''}
    diningroom={'name':'Dining Room','directions':dirs,'msg':''}
    bedroom={'name':'Bedroom','directions':dirs,'msg':''}
    

    #directions(N,E,S,W)
    entrance['directions']=(livingroom,kitchen,0,0)
    livingroom['directions']=(0,diningroom,entrance,corridor)
    corridor['directions']=(bedroom,livingroom,0,0)
    kitchen['directions']=(diningroom,0,0,entrance)
    diningroom['directions']=(0,0,kitchen,livingroom)
    bedroom['directions']=(0,0,corridor,0)
    
    
    #places where basket can be placed
    rooms=[livingroom,corridor,kitchen,diningroom,bedroom]
    rooms_with_basket=random.choice(rooms)
    eggs_delivered=False
    room=entrance
    print(room['name'])
    print("Welcome bunny! Can you find the basket?")

    #Searching the basket
    while True:
        
        if eggs_delivered and room['name']=="Entrance":
            print('You\'ve delivered the basket and found your way back to the entrance.\n Congratulations. You can leave.')
            break;
        elif not eggs_delivered and room['name']==rooms_with_basket['name']:
            eggs_delivered=True
            print(msg(room) + "You\'ve found the basket and delivered the eggs.\n Now find your way back to the entrance.")
            room['msg']='You are back in the '+ room['name']+'!\n You\'ve already delivered the eggs. Make your way back to the entrance quickly'
        else:
            print(msg(room))
            room['msg']='You are back in the '+ room['name']


        stuck=True
        dir=input("Which direction do you want to go:N,E,S,W? Q to Quit >> ")
        if dir == 'Q':
            print("Oh! So you did not wanted to try... Bye Now!!!")
            break;
        choice=get_choice(room,dir)
        
        if choice==-1:
            print("Please enter N,E,S or W")
        elif choice==4:
            print("You cannot go in that direction")
        else:
            room=room['directions'][choice]
            stuck=False
main()
