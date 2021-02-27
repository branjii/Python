#!/usr/bin/env python3

#Author *** Brandon Vajda ***
#Date ***  Feb 22, 2021 ***

#Purpose *** A text based chose your own adventure style game ***

import random

def play_again():
    print('\nDo you wish to play again? (y or n)')
    answer=input('>').lower()

    if "y" in answer:
        #Starts program again for user
        start()
    else:
        #exits the program is user types anything other than "y" or "Y"
        exit()

def invalid_selection(reason):
    #function for displaying game over or invalid selection
    print("\n" + reason)
    print('\ngame over!')
    play_again()

def boss_room():
    class Player:
        def __init__(self):
            self.hp = 9.5
    
    class Warlock:
        def __init__(self):
            self.name = "Warlock"
            self.hp = 12

    warlock = Warlock()
    player = Player()
    warlockHP = warlock.hp
    playerHP = player.hp
    
    print('========================================================================================================================')
    print('\nThis is the boss room, You encounter a ' + Warlock.__name__ + '! You must fight him to escape. He has ' + str(warlockHP) + 'HP! you have ' + str(playerHP) + 'HP!')
    print('\n========================================================================================================================')
    while player.hp > 0 or warlock.hp > 0:
        
        attack=input('Press A to attack > ').lower()
        #Randomly sets player and warlock damage each turn
        playerDMG = random.randint(3,5)
        warlockDMG = random.randint(1,3)
        if attack != "A" and attack != "a":
            print('Please enter only "a" or "A"')
            continue

        if attack == "a":
            
            warlock.hp = warlock.hp - playerDMG
            warlockHP = warlock.hp
            
            print('\nYou use the torch like club and hit the Warlock in the head. You dealt ' + str(playerDMG) + ' damage!')
            
            print('The Warlock now has ' + str(warlockHP) + 'HP')
            print('----------------------------------------------------------------------------------------------')
        if warlock.hp <= 0:
            print('\nCongragulations!')
            invalid_selection("You defated the Warlock and escaped from his Dungeon. You wonder in the forest for a while until you see what seems to be a small village ahead.")
        
        if attack == "a":
            player.hp = player.hp - warlockDMG
            playerHP = player.hp
            
            print('\nThe Warlock mummers a spell and casts it torwards you. He dealt ' + str(warlockDMG) + ' damage!')
            print('You now have ' + str(playerHP) + 'HP')
            print('----------------------------------------------------------------------------------------------')
        if player.hp <= 0:
            print('The Warlock has kocked you out.')
            invalid_selection("You find yourself in a familar cold, wet & dark room.")
        

    

def goblin_room():
    print('========================================================================================================================')
    print("The door is big and heavy, much bigger than any human would need. It creeks loudly as you struggle to push it open, you manage to open it just enough for you to slip through into the room")
    print("\nThere are torches spread out along the wall, similar to the one you hold except huge. They illuminate this great hall. As your eyes adjust to the change in lighting, you see a throne made of stone. It's too big for a man to sit in.")
    print("\nThe ground begins to rumble, something is coming into the hall. Out comes this great big Goblin, a crown made of bones and skulls rests on its head. It takes a seat in its throne.")
    print("\n'Oh forgotten one.... It has been ages since I've had a decent meal..... don't worry though, your fate is in your own hands. If you can guess what number I'm thinking of between 1 and 3, I shall let you pass. You have 2 attempts, should you fail.... your skull will be a nice addition to my crown.")
    print('\n========================================================================================================================')
    number=random.randint(1,3)
    counter=1
    while (counter != 3):
       
        guess=input("Guess " + str(counter) + " >")
        counter+=1
        if (guess == str(number)):
            
            print('\n..... I really need to learn how to count higher than 3.... continue on through the door behind me forgotten one.....\n')
            boss_room()
        elif ((guess < str(1)) and (guess > str(3))):
            print('\ngggrrrrr.... please I dont understand those numbers..... guess again.')
            counter-=1
        elif counter == 2:
            print('\nYou have 1 more guess..... think carefully....\n')
    invalid_selection("\nThe golbin king has a feast tonight in your honour. Guess better next time.")

def skeleton_room():
    print('========================================================================================================================')
    print('As you approach the room you hear distant sounds coming from far within the room,\nUpon entering the room you spot a dimly lit, yet beatiful blue flame. Its on the other side of the room, you begin to walk slowly towrards it.\n\nAs the blue wisp of the flame lures your attention, you start to have the feeling of somethign crushing underneath your feet while you walk. The sounds earlier seem to be the rattling of bones. There is something in the darkness, lurking. You are too close to the light now to return.')
    print('\n========================================================================================================================')
    print('What do you do?')
    print('----------------------------------')
    print('1). Ignite torch using the flame?')
    print('2). Continue on in the dark?')
    #take input
    answer = input(">")

    if answer == "1":
        #story & game ends. 
        print('========================================================================================================================')
        print('You ignite the torch with the blue flame, blue light illuminates the floor around you\n\n\n~i t s    a l l   s k e l e t o n   r e m a i n s~\n\n\nThe rattling begins getting louder, something is approaching in the dark. It limps its way out of the void, revealing its decayed & decrepit skull. The blue flame reflecting where its eyes would be.\nSuddenly more blue eyes appear in the darkness around you.')
        print('\n========================================================================================================================')
        invalid_selection("You do not escape the undead.")
    elif answer == "2":
        #lead player to the boss_room()
        print('========================================================================================================================')
        print('\nYou Decided to keep heading forward in the dark trusting only your gut feeling and senses. A wise decision.\n')
        boss_room()
    else:
        invalid_selection("Game over! You lost cause you can't type properly, idiot.")

def start():
    #Intro to game
    print('========================================================================================================================')
    print('Welcome brave adventurer.... Lets see how your story unfolds....')
    print('\n========================================================================================================================')
    answer = input("\nYou wake up to darkness, nothing but the abyss. It's cold and wet, you can hear the sound of water dripping, you must be underground.\n\nYou feel your way around the room and find what seems to be a burnt torch, you decide to take it.\n\nYou have discovered there are two paths, you must find a way out of here. What room do you venture into, right or left? (R/L): ").lower()
    if "l" in answer:
        #if player typed "left" or "l" lead them to skeleton_room()
        skeleton_room()
    elif "r" in answer:
        #if player typed "right" or "r" lead them to goblin_room()
        goblin_room()
    else:
        invalid_selection("You don't know how to type properly.")

#starts the game
start()

