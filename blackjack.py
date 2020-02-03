#!/usr/bin/env python3
#blackjack.py

import random
import os
cards= [ "2","3","4","5","6","7","8","9","10","J","Q","K","A"]*4

dealer_hand=[]
your_hand=[]

def generator(hands):
    value=0
    k=len(hands)
    for i in range(k):               
        if hands[i] in "JQK":
            value+=10
        elif hands[i] not in "JQKA":
            value+=int(hands[i])
        elif hands[i] == "A":
            value+=1

    if value<12 and "A" in hands:
        value+=10

    return value

def play():
    random.shuffle(cards)

    dealer_hand.append(cards.pop())
    dealer_hand.append(cards.pop())
    your_hand.append(cards.pop())
    your_hand.append(cards.pop())
    os.system("cls")
    print("Your hand:     ", "-".join(your_hand)," value", generator(your_hand))
    print("Dealer's hand: ", dealer_hand[0]+"-xx", "value ", generator(dealer_hand[0]),"\n")

play()
while True:
    if generator(your_hand)==21:
        print("You win! BlackJack")
        break
    if generator(your_hand)>21:
        print("You Lose!")
        break
    answer=input("Hit or Stay: ")
    print("")
    if answer.lower()=="stay":
        while generator(dealer_hand) <17 or generator(your_hand)>=generator(dealer_hand) :
            dealer_hand.append(cards.pop())
        if generator(dealer_hand)<=21:
            os.system("cls")
            print("Your hand:     ", "-".join(your_hand),"value:", generator(your_hand))
            print("Dealer's hand: ","-".join(dealer_hand), "value:", generator(dealer_hand),"\nYou Lose!\n")
        else:
            os.system("cls")
            print("Your hand:     ", "-".join(your_hand),"value:", generator(your_hand))
            print("Dealer's hand: ","-".join(dealer_hand), "value:", generator(dealer_hand),"\nYou Win!\n")
        break
    elif answer.lower()=="hit":
        os.system("cls")
        your_hand.append(cards.pop())
        print("Your hand:     ", "-".join(your_hand),"value: ", generator(your_hand))
        print("Dealer's hand: ", dealer_hand[0]+"-xx", "value: ", generator(dealer_hand[0]),"\n")
        continue
    else:
        continue
