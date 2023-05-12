
from controller_2 import *


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()
    #def submit_score
# player_score = 0
# num_dice_taken = 0
# if not score_list:
#     return 0
#
# player_score += self.point_check(score_list)
# self.score_goal.setText(f"points {player_score}")
# num_dice_taken = len(score_list)
# print(player_score)
# print(num_dice_taken)
# self.new_roll(self.num_dice - num_dice_taken)
# if num_dice_taken >= 6:
#     self.new_roll_button.setVisible(True)
#     num_dice_taken = 0
# #num_dice_taken = 0
# #score_list.clear()
# return num_dice_taken


#def new_roll(self,num_dice):
# self.dice1.setEnabled(True)
# self.dice2.setEnabled(True)
# self.dice3.setEnabled(True)
# self.dice4.setEnabled(True)
# self.dice5.setEnabled(True)
# self.dice6.setEnabled(True)
# self.dice1.setVisible(False)
# self.dice2.setVisible(False)
# self.dice3.setVisible(False)
# self.dice4.setVisible(False)
# self.dice5.setVisible(False)
# self.dice6.setVisible(False)
# for dice in range(0,num_dice):
#     self.dice_roll = self.rand_int_list_generator(num_dice)
#     self.display_dice(self.dice_roll)
# print(self.dice_roll)


#     def start_round(self):
#         # Set up player header label and font
#         font = QtGui.QFont("Arial", 24)
#         self.player_header.setFont(font)
#         self.player_header.setVisible(True)
#         self.score_goal.setVisible(True)
#
#         for player in self.players_list:
#             self.player_header.setText(f"Player {player}'s turn")
#
#             dice_roll = self.rand_int_list_generator(self.num_dice)
#             self.display_dice(dice_roll)
#             points = self.point_check(dice_roll)
#
#             while True:
#                 num_dice_taken = self.submit_score(self.score_list)[0]
#                 if num_dice_taken == 0 or points == 0:
#                     break
#
#                 self.num_dice -= num_dice_taken
#                 print(f"Number of dice taken: {num_dice_taken}")
#                 print(f"Number of dice remaining: {self.num_dice}")
#                 if self.num_dice == 0:
#                     self.submit_score(self.score_list)
#                     break
#
#                 self.player_header.setText('ROLL AGAIN')
#                 dice_roll = self.rand_int_list_generator(self.num_dice)
#                 self.display_dice(dice_roll)
#
#                 points = self.point_check(dice_roll)




