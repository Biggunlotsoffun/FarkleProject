from PyQt5.QtWidgets import *
from view_two import *
from PyQt5.QtGui import *
import random
import time

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.current_player = 0
        self.score_list = []
        self.num_dice = 6
        self.num_dice_taken = 0
        self.selected_dice = []
        self.place_holder = 0

        self.new_points = 0
        self.dice1.setVisible(False)
        self.dice2.setVisible(False)
        self.dice3.setVisible(False)
        self.dice4.setVisible(False)
        self.dice5.setVisible(False)
        self.dice6.setVisible(False)
        self.dice_list = [self.dice1, self.dice2, self.dice3, self.dice4, self.dice5, self.dice6]
        self.dice_buttons = self.dice_list
        self.dice_roll = self.rand_int_list_generator(self.num_dice)
        self.rand_int_list_generator(self.num_dice)
        self.player_header.setVisible(False)
        self.score_goal.setVisible(False)
        self.player1_score.setVisible(False)
        self.player2_score_2.setVisible(False)
        self.player3_score_2.setVisible(False)
        self.player4_score_2.setVisible(False)
        self.player5_score_2.setVisible(False)
        self.player6_score_2.setVisible(False)
        self.player7_score_2.setVisible(False)
        self.player8_score_2.setVisible(False)
        self.player9_score_2.setVisible(False)
        self.player10_score_2.setVisible(False)
        self.player1_score_label.setVisible(False)
        self.player2_score_label_2.setVisible(False)
        self.player3_score_label_2.setVisible(False)
        self.player4_score_label_2.setVisible(False)
        self.player5_score_label_2.setVisible(False)
        self.player6_score_label_2.setVisible(False)
        self.player7_score_label_2.setVisible(False)
        self.player8_score_label_2.setVisible(False)
        self.player9_score_label_2.setVisible(False)
        self.player10_score_label_2.setVisible(False)
        self.score_label_list =[self.player1_score,self.player2_score_2, self.player3_score_2, self.player4_score_2, self.player5_score_2,self.player6_score_2, self.player6_score_2,self.player7_score_2,self.player8_score_2,self.player9_score_2, self.player10_score_2]
        self.players_list = []
        self.rand_int_list = []
        self.player = 0
        self.temp = 0



        image_file = r'farkle_score.png'
        pixmap = QtGui.QPixmap(image_file)
        self.farkle_rules.setPixmap(pixmap.scaled(self.farkle_rules.size(), QtCore.Qt.KeepAspectRatio))
        self.dice1.clicked.connect(self.button_clicked)
        self.dice2.clicked.connect(self.button_clicked)
        self.dice3.clicked.connect(self.button_clicked)
        self.dice4.clicked.connect(self.button_clicked)
        self.dice5.clicked.connect(self.button_clicked)
        self.dice6.clicked.connect(self.button_clicked)
        self.reset_button.clicked.connect(self.reset_dice)
        self.submit_button.clicked.connect(lambda: self.submit_score())
        self.new_roll_button.clicked.connect(lambda: self.new_roll(6))
        self.new_roll_button.setVisible(False)
        self.reset_button.setVisible(False)
        self.submit_button.setVisible(False)
        self.bank_button.clicked.connect(self.bank_player_points)
        self.bank_button.setVisible(False)
        self.player_count.addItem('select players')
        self.player_count.addItem('2 players')
        self.player_count.addItem('3 players')
        self.player_count.addItem('4 players')
        self.player_count.addItem('5 players')
        self.player_count.addItem('6 players')
        self.player_count.addItem('7 players')
        self.player_count.addItem('8 players')
        self.player_count.addItem('9 players')
        self.player_count.addItem('10 players')
        self.player_count.addItem('Reset')
        self.player_count.currentIndexChanged.connect(self.num_players_selected)
        self.submit_player_num.clicked.connect(self.lets_play)

    def bank_player_points(self):
        current_score = self.score_label_list[self.player].value()
        new_score = current_score + self.temp + self.button_clicked_temp
        self.score_label_list[self.player].display(new_score)
        if new_score >= 10000:
            self.player_header.setText(f"Player {self.player + 1} Wins!!!")
            self.disable_bank_reset_submit_buttons()
        else:
            self.temp = 0
            self.player += 1
            if self.player >= len(self.players_list):
                self.player = 0
            self.num_dice = 6
            self.score_list.clear()
            self.place_holder = 0


            self.reset_dice()
            self.start_round()




    def new_roll(self,num_dice):
        self.dice1.setEnabled(True)
        self.dice2.setEnabled(True)
        self.dice3.setEnabled(True)
        self.dice4.setEnabled(True)
        self.dice5.setEnabled(True)
        self.dice6.setEnabled(True)
        self.dice1.setVisible(False)
        self.dice2.setVisible(False)
        self.dice3.setVisible(False)
        self.dice4.setVisible(False)
        self.dice5.setVisible(False)
        self.dice6.setVisible(False)
        self.dice_roll = self.rand_int_list_generator(num_dice)
        self.display_dice(self.dice_roll)


        return self.dice_roll

    def disable_bank_reset_submit_buttons(self):
        self.bank_button.setEnabled(False)
        self.reset_button.setEnabled(False)
        self.submit_button.setEnabled(False)

    def lets_play(self):
        self.dice1.setVisible(True)
        self.dice2.setVisible(True)
        self.dice3.setVisible(True)
        self.dice4.setVisible(True)
        self.dice5.setVisible(True)
        self.dice6.setVisible(True)
        self.num_of_players.setVisible(False)
        self.player_count.setVisible(False)
        self.reset_button.setVisible(True)
        self.submit_button.setVisible(True)
        self.submit_player_num.setVisible(False)
        self.bank_button.setVisible(True)
        self.start_round()

    def reset_dice(self):
        self.dice1.setEnabled(True)
        self.dice2.setEnabled(True)
        self.dice3.setEnabled(True)
        self.dice4.setEnabled(True)
        self.dice5.setEnabled(True)
        self.dice6.setEnabled(True)
        self.button_clicked_temp = 0
        self.score_list = []

    def button_clicked(self):
        button = self.sender()
        value = button.my_value
        button.setEnabled(False)
        self.score_list.append(value)
        print(self.score_list)
        print(value)
        self.button_clicked_temp = self.point_check(self.score_list)


    def submit_score(self):
        #self.temp += self.point_check(self.dice_roll)
        self.players_list[self.player] = self.temp
        self.button_clicked_temp = 0
        num_dice = 6


        if len(self.score_list) < 6:
            self.place_holder += len(self.score_list)
            self.num_dice_taken = self.place_holder
            y = self.new_roll(self.num_dice-self.num_dice_taken)
            x = self.point_check(y)
            self.temp += self.point_check(self.score_list)
            print(y)
            print(f"new score: {x}")
            self.score_goal.setText(f"points {x}")


            self.score_list.clear()
            if x ==0:
                self.player += 1
                if self.player >= len(self.players_list):
                    self.player = 0
                self.score_list.clear()
                self.num_dice = 6
                self.place_holder = 0
                self.score_list.clear()
                self.bank_player_points()

        else:
            self.num_dice_taken = len(self.score_list)

            y = self.new_roll(6)
            x = self.point_check(y)
            #self.temp += self.point_check(y)
            self.temp += self.point_check(self.score_list)
            self.score_goal.setText(f"points {x}")

            print(f"new score: {x}")

            self.score_list.clear()
            if x == 0:
                self.player += 1
                if self.player >= len(self.players_list):
                    self.player = 0
                self.num_dice =6
                self.place_holder= 0
                self.score_list.clear()
                self.bank_player_points()

    def enable_dice(self):
        for die in self.dice_list:
            die.setEnabled(True)

    def enable_dice_buttons(self):
        for button in self.dice_buttons:
            button.setEnabled(True)



    def start_round(self):
        # Set up player header label and font
        font = QtGui.QFont("Arial", 24)
        self.player_header.setFont(font)
        self.player_header.setVisible(True)
        self.score_goal.setVisible(True)
        dice_roll = self.rand_int_list_generator(self.num_dice)
        self.display_dice(dice_roll)
        x = self.point_check(dice_roll)
        if x == 0:
            self.player += 1
            if self.player >= len(self.players_list):
                self.player = 0
            self.start_round()
        self.score_goal.setText(f"points {x}")
        self.player_header.setText(f"Player {self.player + 1}'s turn")

    def display_dice(self, rand_int_list):

        for i in range(len(rand_int_list)):
            if rand_int_list[i] == 1:
                image_file = r'1_dice.png'
            elif rand_int_list[i] == 2:
                image_file = r'2_dice.png'
            elif rand_int_list[i] == 3:
                image_file = r'3_dice.png'
            elif rand_int_list[i] == 4:
                image_file = r'4_dice.png'
            elif rand_int_list[i] == 5:
                image_file = r'5_dice.png'
            elif rand_int_list[i] == 6:
                image_file = r'6_dice.png'
            else:
                image_file = ''

            pixmap = QPixmap(image_file)
            icon = QIcon(pixmap)
            self.dice_list[i].setVisible(True)
            self.dice_list[i].setIcon(icon)
            self.dice_list[i].my_value = rand_int_list[i]

    def rand_int_list_generator(self, num_dice):
        if num_dice == 6:
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            d3 = random.randint(1,6)
            d4 = random.randint(1,6)
            d5 = random.randint(1,6)
            d6 = random.randint(1,6)
            self.rand_int_list = [d1,d2,d3,d4,d5,d6]

        elif num_dice == 5:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            d3 = random.randint(1, 6)
            d4 = random.randint(1, 6)
            d5 = random.randint(1, 6)
            self.rand_int_list = [d1, d2, d3, d4, d5,]

        elif num_dice == 4:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            d3 = random.randint(1, 6)
            d4 = random.randint(1, 6)
            self.rand_int_list = [d1, d2, d3, d4,]

        elif num_dice == 3:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            d3 = random.randint(1, 6)
            self.rand_int_list = [d1, d2, d3,]

        elif num_dice == 2:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            self.rand_int_list = [d1, d2,]

        elif num_dice == 1:
            d1 = random.randint(1,6)
            self.rand_int_list = [d1]
        return self.rand_int_list
    def one_hundreds(self,dice_roll):
        #dice_roll = self.rand_int_list
        one_score = 0
        has_one = False
        for i in range(len(dice_roll)):
            if dice_roll[i] == 1:
                one_score += 100
                has_one = True
        if has_one:
            return one_score, True
        else:
            return 0, False


    def fifties(self,dice_roll):
        #dice_roll = self.rand_int_list
        fifty_score = 0
        has_fifty = False
        for i in range(len(dice_roll)):
            if dice_roll[i] == 5:
                fifty_score += 50
                has_fifty = True
        if has_fifty:
            return fifty_score, True
        else:
            return 0, False

    def of_a_kind(self,dice_roll):
        #dice_roll = self.rand_int_list
        kind_dict = {}
        kind_score = 0
        has_kind = False
        for i in dice_roll:
            kind_dict[i] = kind_dict.get(i,0)+1
        for keys, values in kind_dict.items():
            if values == 3:
                if keys == 1:
                    kind_score = 300
                    has_kind = True
                else:
                    kind_score = keys * 100
                    has_kind = True
            if values == 4:
                kind_score = 1000
                has_kind = True
            if values == 5:
                kind_score = 2000
                has_kind = True
            if values == 6:
                kind_score = 3000
                has_kind = True
        if has_kind:
            return kind_score, True
        else:
            return 0, False

    def straight(self,dice_roll):
        #dice_roll = self.rand_int_list
        straight_score = 0
        straight_dict = {}
        straight_counter = 0
        has_straight = False
        for i in dice_roll:
            straight_dict[i] = straight_dict.get(i,0)+1
        for keys, values in straight_dict.items():
            if values == 1:
                straight_counter += 1
        if straight_counter == 6:
            straight_score = 1500
            has_straight = True
        if has_straight:
            return straight_score, True
        else:
            return 0, False

    def three_pairs(self,dice_roll):
        #dice_roll = self.rand_int_list
        three_pairs_score = 0
        three_pairs_dict = {}
        three_pairs_counter = 0
        has_pairs = False
        for i in dice_roll:
            three_pairs_dict[i] = three_pairs_dict.get(i, 0) + 1
        for keys, values in three_pairs_dict.items():
            if values == 2:
                three_pairs_counter += 1
        if three_pairs_counter == 3:
            three_pairs_score = 1500
            has_pairs = True
        if has_pairs:
            return three_pairs_score, True
        else:
            return 0, False

    def two_triplets(self,dice_roll):
        #dice_roll = self.rand_int_list
        triplet_score = 0
        triplet_dict = {}
        triplet_counter = 0
        has_trip = False
        for i in dice_roll:
            triplet_dict[i] = triplet_dict.get(i, 0) + 1
        for keys, values in triplet_dict.items():
            if values == 3:
                triplet_counter += 1
        if triplet_counter == 2:
            triplet_score = 2500
        if has_trip:
            return triplet_score, True
        else:
            return 0, False

    def four_plus_pair(self,dice_roll):
        #dice_roll = self.rand_int_list
        four_pair_score = 0
        four_pair_dict = {}
        has_pair = False
        for i in dice_roll:
            four_pair_dict[i] = four_pair_dict.get(i, 0) + 1
        for keys, values in four_pair_dict.items():
            if values == 4 and any(val == 2 for val in four_pair_dict.values()):
                four_pair_score = 1500
                has_pair = True
        if has_pair:
            return four_pair_score, True
        else:
            return 0, False

    def point_check(self,dice_roll):
        points = 0
        #dice_roll = self.rand_int_list
        ones = self.one_hundreds(dice_roll)[0]
        fifties = self.fifties(dice_roll)[0]
        kind = self.of_a_kind(dice_roll)[0]
        straight = self.straight(dice_roll)[0]
        three_pair = self.three_pairs(dice_roll)[0]
        two_trips = self.two_triplets(dice_roll)[0]
        four_and_two = self.four_plus_pair(dice_roll)[0]


        if self.one_hundreds(dice_roll)[1] is True:
            if ones < 300:
                points += ones
        if self.fifties(dice_roll)[1] is True:
            if fifties < 150:
                points += fifties
        if self.four_plus_pair(dice_roll)[1] is True:
            points = four_and_two
            return points
        if self.of_a_kind(dice_roll)[1] is True:
            points += kind
            return points
        if self.two_triplets(dice_roll)[1] is True:
            points = two_trips
            return points
        if self.three_pairs(dice_roll)[1] is True:
            points = three_pair
            return points
        if self.straight(dice_roll)[1] is True:
            points = straight
            return points
        return points

    def num_players_selected(self, index):
        num_players = index
        if num_players == 1:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.players_list = [0, 0]
        elif num_players == 2:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player3_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.player3_score_2.setVisible(True)
            self.players_list = [0, 0, 0]
        elif num_players == 3:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player3_score_label_2.setVisible(True)
            self.player4_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.player3_score_2.setVisible(True)
            self.player4_score_2.setVisible(True)
            self.players_list = [0, 0, 0, 0]
        elif num_players == 4:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player3_score_label_2.setVisible(True)
            self.player4_score_label_2.setVisible(True)
            self.player5_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.player3_score_2.setVisible(True)
            self.player4_score_2.setVisible(True)
            self.player5_score_2.setVisible(True)
            self.players_list = [0, 0, 0, 0, 0]
        elif num_players == 5:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player3_score_label_2.setVisible(True)
            self.player4_score_label_2.setVisible(True)
            self.player5_score_label_2.setVisible(True)
            self.player6_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.player3_score_2.setVisible(True)
            self.player4_score_2.setVisible(True)
            self.player5_score_2.setVisible(True)
            self.player6_score_2.setVisible(True)
            self.players_list = [0, 0, 0, 0, 0, 0]
        elif num_players == 6:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player3_score_label_2.setVisible(True)
            self.player4_score_label_2.setVisible(True)
            self.player5_score_label_2.setVisible(True)
            self.player6_score_label_2.setVisible(True)
            self.player7_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.player3_score_2.setVisible(True)
            self.player4_score_2.setVisible(True)
            self.player5_score_2.setVisible(True)
            self.player6_score_2.setVisible(True)
            self.player7_score_2.setVisible(True)
            self.players_list = [0, 0, 0, 0, 0, 0, 0]
        elif num_players == 7:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player3_score_label_2.setVisible(True)
            self.player4_score_label_2.setVisible(True)
            self.player5_score_label_2.setVisible(True)
            self.player6_score_label_2.setVisible(True)
            self.player7_score_label_2.setVisible(True)
            self.player8_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.player3_score_2.setVisible(True)
            self.player4_score_2.setVisible(True)
            self.player5_score_2.setVisible(True)
            self.player6_score_2.setVisible(True)
            self.player7_score_2.setVisible(True)
            self.player8_score_2.setVisible(True)
            self.players_list = [0, 0, 0, 0, 0, 0, 0, 0]
        elif num_players == 8:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player3_score_label_2.setVisible(True)
            self.player4_score_label_2.setVisible(True)
            self.player5_score_label_2.setVisible(True)
            self.player6_score_label_2.setVisible(True)
            self.player7_score_label_2.setVisible(True)
            self.player8_score_label_2.setVisible(True)
            self.player9_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.player3_score_2.setVisible(True)
            self.player4_score_2.setVisible(True)
            self.player5_score_2.setVisible(True)
            self.player6_score_2.setVisible(True)
            self.player7_score_2.setVisible(True)
            self.player8_score_2.setVisible(True)
            self.player9_score_2.setVisible(True)
            self.players_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif num_players == 9:
            self.player1_score_label.setVisible(True)
            self.player2_score_label_2.setVisible(True)
            self.player3_score_label_2.setVisible(True)
            self.player4_score_label_2.setVisible(True)
            self.player5_score_label_2.setVisible(True)
            self.player6_score_label_2.setVisible(True)
            self.player7_score_label_2.setVisible(True)
            self.player8_score_label_2.setVisible(True)
            self.player9_score_label_2.setVisible(True)
            self.player10_score_label_2.setVisible(True)
            self.player1_score.setVisible(True)
            self.player2_score_2.setVisible(True)
            self.player3_score_2.setVisible(True)
            self.player4_score_2.setVisible(True)
            self.player5_score_2.setVisible(True)
            self.player6_score_2.setVisible(True)
            self.player7_score_2.setVisible(True)
            self.player8_score_2.setVisible(True)
            self.player9_score_2.setVisible(True)
            self.player10_score_2.setVisible(True)
            self.players_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif num_players == 10:
            self.player1_score.setVisible(False)
            self.player2_score_2.setVisible(False)
            self.player3_score_2.setVisible(False)
            self.player4_score_2.setVisible(False)
            self.player5_score_2.setVisible(False)
            self.player6_score_2.setVisible(False)
            self.player7_score_2.setVisible(False)
            self.player8_score_2.setVisible(False)
            self.player9_score_2.setVisible(False)
            self.player10_score_2.setVisible(False)
            self.player1_score_label.setVisible(False)
            self.player2_score_label_2.setVisible(False)
            self.player3_score_label_2.setVisible(False)
            self.player4_score_label_2.setVisible(False)
            self.player5_score_label_2.setVisible(False)
            self.player6_score_label_2.setVisible(False)
            self.player7_score_label_2.setVisible(False)
            self.player8_score_label_2.setVisible(False)
            self.player9_score_label_2.setVisible(False)
            self.player10_score_label_2.setVisible(False)