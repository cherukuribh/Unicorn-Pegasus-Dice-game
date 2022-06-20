# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:44:17 2022

@author: skondaveeti9
"""

import random
 
def play_unicornorpegasus(game):
    """ get started with the game you have 
            selected unicorn or pegasus.
     Keep rolling a dice until we collect 
        all the body parts of a unicorn or pegasus."""
    count_body = 0
    count_tail = 0
    count_leg = 0
    count_head = 0
    count_eye = 0
    count_mouth = 0
    count_horn = 0
    count_wing = 0
    rolls = 0
    count_rolls_horn = 0
    count_rolls_wing = 0
    roll_dice = 0
    while (roll_dice!=1):
        roll_dice = random.randint(1,8)
        print('output of rolling a dice ', rolls+1 ,'times is',roll_dice)
        if (roll_dice == 8):
            count_rolls_horn += 1
        if (roll_dice == 7):
            count_rolls_wing += 1
        rolls +=1
    count_body += 1
    print('well done you collected a body')
    print('number of rolls to get body : ',rolls)
    dice = True
    while (dice):
        roll_dice = random.randint(1,8)
        print('output of rolling a dice ', rolls+1 ,'times is',roll_dice)
        rolls +=1
        if (roll_dice == 8):
            count_rolls_horn += 1
        if (roll_dice == 7):
            count_rolls_wing += 1
        if (roll_dice == 2 and count_tail == 0):
            count_tail += 1
            print("we got ",count_tail," tail ")
        elif(roll_dice == 3 and count_leg < 4):
            count_leg += 1
            print("we got ",count_leg," leg ")
        elif(roll_dice == 4 and count_head == 0):
            count_head += 1
            print("we got ",count_head," head ")
        elif(roll_dice == 5 and count_head == 1 and count_eye < 2):            
            count_eye += 1
            print("we got ",count_eye," eye ")
        elif(roll_dice == 6 and count_head == 1 and count_mouth < 1):
            count_mouth += 1
            print("we got ",count_mouth," mouth ")
        elif(roll_dice == 8 and count_head == 1 and game == "unicorn" and count_horn < 1 ):
            count_horn += 1
            print("we got ",count_horn," horn ")
        elif(roll_dice == 7 and count_head == 1 and count_wing < 2 and game == "pegasus"):
            count_wing += 1
            print("we got ",count_wing," wing ")
        elif(count_body == 1 and count_tail == 1 and count_leg == 4 and
           count_head == 1 and count_eye == 2 and count_mouth == 1 and count_horn == 1):
            dice = False
            print('well done you have collected all the body_parts of unicorn')
            print("collected : body-1,tail-1,leg-4,head-1,eye-2,mouth-1,horn-1")
            print('number of rolls to get all the body_parts of unicorn : ',rolls)
            print('number of times we get wings while we roll the dice through out the game:',count_rolls_wing)
            print('number of times we get horn while we roll the dice through out the game:',count_rolls_horn)
        elif(count_body == 1 and count_tail == 1 and count_leg == 4 and
           count_head == 1 and count_eye == 2 and count_mouth == 1 and count_wing == 2):
            dice = False
            print('well done you have collected all the body_parts of pegasus') 
            print("collected : body-1,tail-1,leg-4,head-1,eye-2,mouth-1,wing-2")
            print('number of rolls to get all the body_parts of pegasus : ',rolls)
            print('number of times we get wings while we roll the dice through out the game:',count_rolls_wing)
            print('number of times we get horn while we roll the dice through out the game:',count_rolls_horn)
        else:
            print("not a valid dice roll")
    return()

print(" welcome to Unicorn vs Pegasus dice game ")    
print(" Here we aim to collect all the body parts of a Unicorn or a Pegasus ")
print(" By rolling an 8 sided dice we collect the body parts.The information given below ")
Body_parts = { 1 : 'body',
          2 : 'tail',
          3 : 'leg',
          4 : 'head',
          5 : 'eye',
          6 : 'mouth',
          7 : 'wing',
          8 : 'horn' }
         
for k in Body_parts:
    print(k," gives a " ,Body_parts[k])
    
print(" enter unicorn to play unicorn game /n body parts to be collected for Unicorn ")
print("body-1,tail-1,leg-4,head-1,eye-2,mouth-1,horn-1")

print(" enter pegasus to play pegasus game /n body parts to be collected for Pegasus ")
print("body-1,tail-1,leg-4,head-1,eye-2,mouth-1,wing-2")
      
     
game=input("enter the input to select unicorn or pegasus to play the dice game : ")

print('we are building ',game,'die game')

if(game == 'unicorn' or game == 'pegasus'):
    print("start dice game")
    play_unicornorpegasus(game)
    print("played game succesfully ")
else:
    print("invalid game selection")
   


