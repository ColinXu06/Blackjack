import random
import time

def play_game():
  cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
  #Dealer's cards
  dealer_first_card = random.choice(cards)
  dealer_second_card = random.choice(cards)
  dealer_third_card = random.choice(cards)
  dealer_fourth_card = random.choice(cards)

  #Calculate dealer's score
  dealer_hand = dealer_first_card + dealer_second_card
  if dealer_first_card == 11 and dealer_hand > 21:
    dealer_first_card = 1
  if dealer_second_card == 11 and dealer_hand > 21:
    dealer_second_card = 1
#Player's cards
  first_card = random.choice(cards)
  second_card = random.choice(cards)
  third_card = random.choice(cards)
  fourth_card = random.choice(cards)

#Adjusting player's initial score for aces
  player_hand = first_card + second_card
  if first_card == 11 and player_hand > 21:
    first_card = 1
  if second_card ==11 and player_hand > 21:
    second_card = 1

#Execution starts here
  print("Hello! Welcome to the Python Blackjack Table!")
  time.sleep(1.5)
  print("You are going to be dealt by a completely automated dealer!")
  time.sleep(1)
  print("Are you ready?")
  time.sleep(1.5)

#Make start button later

#Player initial score run
  print(f"Your first card is: {first_card}")
  time.sleep(0.5)
  print(f"Your second card is: {second_card}")
  time.sleep(0.5)
  print(f"Your score is currently: {player_hand}")
  if first_card == 11 or second_card == 11:
    print("Remember, your Ace counts as 1 point if you exceed a score of 21")
  if player_hand == 21:
    print("Blackjack! You win the game")

#Dealer's first card
  print(f"The Dealer's first card is {dealer_first_card}")

#Hit or Stand
  hit = input("Do you want to hit? (yes/no)")

#If player hits
  if hit == "yes":
    player_hand += third_card
    if third_card == 11 and player_hand > 21:
      third_card = 1
    print(f"You drew a: {third_card}, your hand is now: {player_hand}")
    if player_hand > 21:
      print("You bust! dealer wins.")
      return
    hit = input("Do you want to hit? (yes/no)")
    if hit == "yes":
      player_hand += fourth_card
      if fourth_card == 11 and player_hand > 21:
        fourth_card = 1
      print(f"You drew a: {fourth_card}, your hand is now: {player_hand}")
      if player_hand > 21:
        print("You bust! dealer wins.")
        return

#Dealer's turn
  time.sleep(1)
  print(f"The dealer's second card was: {dealer_second_card}, his hand is now: {dealer_hand}")
  
  while dealer_hand < 17:
    dealer_hand += dealer_third_card
    if dealer_third_card == 11 and dealer_hand > 21:
      dealer_third_card = 1
    time.sleep(1)
    print(f"The dealer hits, drawing a: {dealer_third_card}, his hand is now: {dealer_hand}.")

#Determine winner
  if dealer_hand > 21 or player_hand <=21 and player_hand > dealer_hand:
    time.sleep(1.5)
    print(f"You won!, your hand was: {player_hand}, and the dealer's hand was: {dealer_hand}")
  else:
    time.sleep(1.5)
    print(f"You lost!, your hand was: {player_hand}, and the dealer's hand was: {dealer_hand}.")
#Make hit and stand button later

while True:
  play_game()
  play_again = input("Do you want to play again? (yes/no): ").strip().lower()
  if play_again != "yes":
    print("Thanks for playing! Goodbye!")
    break
  print("Let's play again!")
