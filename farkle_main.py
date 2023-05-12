import random
from farkle_functions import *

player_num = int(input("Enter number of players: "))
game = FarkleGame(6,player_num)

if player_num == 1:
    game.add_player("Player 1")
    game.add_player("Computer")
else:
    for i in range(1, player_num + 1):
        game.add_player(f"Player {i}")

while True:
    game.start_round()
    for player in game.players:
        if not player.is_computer:
            print(f"\nIt's {player.name}'s turn.")
            print(f"You have {player.score} points so far.")
            dice_roll = game.roll_dice()
            print(f"Your roll: {dice_roll}")
            turn_score = player.play_turn(dice_roll)
            print(f"You scored {turn_score} points this turn.")
            if player.score >= game.goal_score:
                print(f"Congratulations, {player.name}! You won!")
                exit()

    if game.players[-1].score >= game.goal_score:
        print(f"Congratulations, {game.players[-1].name}! You won!")
        exit()

# def point_check(dice_roll):
#     ones = farkle_functions.one_hundreds(dice_roll)
#     fifties = farkle_functions.fifties(dice_roll)
#     kind = farkle_functions.of_a_kind(dice_roll)
#     straight = farkle_functions.straight(dice_roll)
#     three_pair = farkle_functions.three_pairs(dice_roll)
#     two_trips = farkle_functions.two_triplets(dice_roll)
#     four_and_two = farkle_functions.four_plus_pair(dice_roll)
#     if len(dice_roll) == 6:
#         if ones[1]:
#             print(f"The ones points are: {ones[0]}")
#         if fifties[1]:
#             print(f"The Fifties points are: {fifties[0]}")
#         if kind[1]:
#             print(f"you got {kind[0]} points of a kind")
#         if straight[1]:
#             print(f"you got a straight! {straight[0]} points")
#         if three_pair[1]:
#             print(f"you got 3 pairs! worth {three_pair[0]} points")
#         if two_trips[1]:
#             print(f"You got two triplets worth {two_trips[0]} points")
#         if four_and_two[1]:
#             print(f"You got a pair and four of a kind! points: {four_and_two[0]}")
#     elif 3 <= len(dice_roll) <= 5:
#         if ones[1]:
#             print(f"The ones points are: {ones[0]}")
#         if fifties[1]:
#             print(f"The Fifties points are: {fifties[0]}")
#         if kind[1]:
#             print(f"you got {kind[0]} points of a kind")
#     else:
#         if ones[1]:
#             print(f"The ones points are: {ones[0]}")
#         if fifties[1]:
#             print(f"The Fifties points are: {fifties[0]}")
#
#
# player_num = int(input("Enter num of players: "))
# player_list = []
# for i in range(1,(player_num+1)):
#     player_list.append(i)
# #print(player_list)
# if player_num == 1:
#     player_list = [0,1]
# num_dice_taken = 0
# #print("Lets play!")
# dice_roll = farkle_functions.rand_int_list_generator(6)
# print(dice_roll)
# print(len(dice_roll))
# print(point_check(dice_roll))
# if player_num != 1:
#     for i in range(len(player_list)):
#         print(dice_roll)
#         die_pos = []
#         number = input("enter which dice positions you want to keep: ")
#         while number != "q":
#             die_pos.append(number)
#             number = input("enter which dice positions you want to keep: ")
#             print("enter q when done")
#            # die_pos.append(numberg)
#         print(die_pos)