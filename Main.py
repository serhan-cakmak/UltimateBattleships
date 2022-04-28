
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE








    #firstly I need to make the board,since our board size doesn't change I just multipply the - char with 10 for 10 times
    player1_board = [[["-" for i in range(10)]for j in range(10)]]
    player2_board = [[["-" for i in range(10)]for j in range(10)]]

    # I wrote the same code for changing the table during war time in game
    player1emptyboard=[[["-" for i in range(10)]for j in range(10)]]
    player2emptyboard=[[["-" for i in range(10)] for j in range(10)]]
    #I took the input in lower so I made a lower case list and dict to reach the length of a spesific ship
    shiplist_lower = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    shiplong_dict = {}
    shiplong_dict["carrier"] = 5
    shiplong_dict["battleship"] = 4
    shiplong_dict["cruiser"] = 3
    shiplong_dict["submarine"] = 3
    shiplong_dict["destroyer"] = 2
    ship_name_list_firstlettercapital = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    # I made a while loop to print out the same table until I want to break
    while len(ship_name_list_firstlettercapital)>0:
        print_3d_list(player1_board+player2_board)


        # I differed 2 if statements to check if list is not empty

        if len(ship_name_list_firstlettercapital)>0:

            print_ships_to_be_placed()



            [print_single_element(i)for i in ship_name_list_firstlettercapital]





            print_empty_line()

            #first player placement
            #I need to take these values inside the for loop to print over and over again
            print_player_turn_to_place(1)
            print_to_place_ships()
            ship_input_string= input().rstrip()
            ship_input_list= ship_input_string.lower().split() # I made it lower for case insensitivity
            ship_input_list= ship_input_list[0:4]  # so if user tries to enter more than 4 , it wont be evaluated


            #checking for conditions

            if len(ship_input_list)<4 :
                print_incorrect_input_format()
                continue
            # to check if the input is not a integer
            try:
                int(ship_input_list[1])
                int(ship_input_list[2])
            except:
                print_incorrect_input_format()
                continue

            if  (int(ship_input_list[1])  not in [i for i in range(1,11)] or int(ship_input_list[2]) not in [i for i in range(1,11)]):
                print_incorrect_coordinates()
                continue

            # name checker with case insensitive manner
            if ship_input_list[0] not in shiplist_lower:
                print_incorrect_ship_name()
                continue


            if ship_input_list[3] not in ["v","h"]:
                print_incorrect_orientation()
                continue


            # removing the ship names from the list enables us to check if the ship is already placed
            if ship_input_list[0] not in [i.lower() for i in ship_name_list_firstlettercapital]:
                print_ship_is_already_placed(ship_input_list[0].lower().title())
                continue

            # I differed h and v because it changes the way we play on a list
            if ship_input_list[3]=="h":
                if  (shiplong_dict[ship_input_list[0]] + int(ship_input_list[1]) not in range (1,12)) :

                    print_ship_cannot_be_placed_outside(ship_input_list[0].lower().title())
                    continue
            #this code below is just a interval that differs with the length of a ship
            if ship_input_list[3]=="h":
                if "#" in player1_board[0][int(ship_input_list[2])-1][int(ship_input_list[1])-1: (int(ship_input_list[1]) + shiplong_dict[ship_input_list[0]]-1)]:
                    print_ship_cannot_be_placed_occupied(ship_input_list[0].lower().title())
                    continue

                else:
                    player1_board[0][int(ship_input_list[2]) - 1][int(ship_input_list[1]) - 1: (int(ship_input_list[1]) + shiplong_dict[ship_input_list[0]] - 1)]= ["#"]* shiplong_dict[ship_input_list[0]]
                    ship_name_list_firstlettercapital.remove(ship_input_list[0].lower().title())

            # same code for vertical placement

            if ship_input_list[3]=="v":
                if (shiplong_dict[ship_input_list[0]] + int(ship_input_list[2]) not in range(1, 12)):
                    print_ship_cannot_be_placed_outside(ship_input_list[0].lower().title())
                    continue




            if ship_input_list[3] == "v":


                if "#" in [player1_board[0][int(ship_input_list[2]) + long - 1][int(ship_input_list[1]) - 1]for long in range(shiplong_dict[ship_input_list[0]])] :
                    print_ship_cannot_be_placed_occupied(ship_input_list[0].lower().title())
                    continue

                # list comprehension cannot be changed  which in the first place I faced with error about it
                else:
                    for long in range(shiplong_dict[ship_input_list[0]]):

                        player1_board[0][int(ship_input_list[2]) + long - 1][int(ship_input_list[1]) - 1] = "#"

                ship_name_list_firstlettercapital.remove(ship_input_list[0].lower().title())


        # end of placement part
        if len(ship_name_list_firstlettercapital)==0:
            print_3d_list(player1_board+player2_board)
            print_confirm_placement()
            yes_no=input().lower()

            while yes_no not in ["n","y"]:
                print_confirm_placement()
                yes_no = input().lower()



            #if the answer is no I must delete the edits and recreate the list

            if yes_no=="n":
                ship_name_list_firstlettercapital = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                player1_board = [[["-" for i in range(10)] for j in range(10)]]


            if yes_no=="y":
                pass
    # This list was empty because of the while loop so I just made another one with same logic
    ship_name_list_firstlettercapital = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

    #this code is the same as the above one except the printing on the 2 player board
    while len(ship_name_list_firstlettercapital) > 0:
        print_3d_list(player1emptyboard + player2_board)



        if len(ship_name_list_firstlettercapital) > 0:

            print_ships_to_be_placed()

            [print_single_element(i) for i in ship_name_list_firstlettercapital]

            print_empty_line()


            print_player_turn_to_place(2)
            print_to_place_ships()
            ship_input_string = input().rstrip()
            ship_input_list = ship_input_string.lower().split()  # I made it lower for case insensitivity
            ship_input_list = ship_input_list[0:4]

            if len(ship_input_list) < 4:
                print_incorrect_input_format()
                continue

            try:
                int(ship_input_list[1])
                int(ship_input_list[2])
            except:
                print_incorrect_input_format()
                continue

            if (int(ship_input_list[1]) not in [i for i in range(1, 11)] or int(ship_input_list[2]) not in [i for i in range(1,11)]):
                print_incorrect_coordinates()
                continue


            if ship_input_list[0] not in shiplist_lower:
                print_incorrect_ship_name()
                continue

            if ship_input_list[3] not in ["v", "h"]:
                print_incorrect_orientation()
                continue

            if ship_input_list[0] not in [i.lower() for i in ship_name_list_firstlettercapital]:
                print_ship_is_already_placed(ship_input_list[0].lower().title())
                continue

            if ship_input_list[3] == "h":
                if (shiplong_dict[ship_input_list[0]] + int(ship_input_list[1]) not in range(1, 12)):
                    print_ship_cannot_be_placed_outside(ship_input_list[0].lower().title())
                    continue

            if ship_input_list[3] == "h":
                if "#" in player2_board[0][int(ship_input_list[2]) - 1][int(ship_input_list[1]) - 1: (int(ship_input_list[1]) + shiplong_dict[ship_input_list[0]] - 1)]:
                    print_ship_cannot_be_placed_occupied(ship_input_list[0].lower().title())
                    continue

                else:
                    player2_board[0][int(ship_input_list[2]) - 1][
                    int(ship_input_list[1]) - 1: (int(ship_input_list[1]) + shiplong_dict[ship_input_list[0]] - 1)] = ["#"] * shiplong_dict[ship_input_list[0]]
                    ship_name_list_firstlettercapital.remove(ship_input_list[0].lower().title())

            if ship_input_list[3] == "v":
                if (shiplong_dict[ship_input_list[0]] + int(ship_input_list[2]) not in range(1, 12)):
                    print_ship_cannot_be_placed_outside(ship_input_list[0].lower().title())
                    continue

            if ship_input_list[3] == "v":
                if "#" in [player2_board[0][int(ship_input_list[2]) + long - 1][int(ship_input_list[1]) - 1]for long in range(shiplong_dict[ship_input_list[0]])] :
                    print_ship_cannot_be_placed_occupied(ship_input_list[0].lower().title())
                    continue

                else:
                    for long in range(shiplong_dict[ship_input_list[0]]):

                        player2_board[0][int(ship_input_list[2]) + long - 1][int(ship_input_list[1]) - 1] = "#"

                ship_name_list_firstlettercapital.remove(ship_input_list[0].lower().title())

        if len(ship_name_list_firstlettercapital) == 0:
            print_3d_list(player1emptyboard + player2_board)
            print_confirm_placement()
            yes_no = input().lower()

            while yes_no not in ["n", "y"]:
                print_confirm_placement()
                yes_no = input().lower()

            if yes_no == "n":
                ship_name_list_firstlettercapital = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                player2_board = [[["-" for i in range(10)] for j in range(10)]]

            if yes_no == "y":
                pass

    #now its time to start the war phase turn variable only change when the player finished his/her turn
    turn=1
    while True:
        if "#" not in [ k for i in player1_board for j in i for k in j]:   # if the all "#"characters have converted to ! that means there is no ship that can be struck
            print_3d_list(player1emptyboard+player2_board)
            print_player_won(2)
            print_thanks_for_playing()
            break

        if "#" not in [ k for i in player2_board for j in i for k in j]:
            print_3d_list(player1_board + player2emptyboard)
            print_player_won(1)
            print_thanks_for_playing()
            break


        # first player's turn
        if turn%2!=0:
            print_3d_list(player1_board+player2emptyboard)
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            strikecoordinats=input().split()
            strikecoordinats = strikecoordinats[0:2]  #if user gives more than 2 arguments excessive ones willbe neglected

            if len(strikecoordinats) != 2:
                print_incorrect_input_format()
                continue

            try:
                int(strikecoordinats[0])
                int(strikecoordinats[1])
            except:
                print_incorrect_input_format()
                continue

            if strikecoordinats[0]  not in ["{}".format(i) for i in range(1, 11)] or strikecoordinats[1] not in [ "{}".format(i) for i in range(1,11)]: #checking if the numbers are between 1 and 10
                print_incorrect_coordinates()
                continue



            ######## I have checked the coordinats so I am sure that x and y are integers (Note: x and y values is reversed because the code I wrote but there wont be problem that user faces)
            y=int(strikecoordinats[0])-1
            x=int(strikecoordinats[1])-1

            if player2emptyboard[0][x][y] in["!","O"]:
                print_tile_already_struck()
                continue

            if  player2_board[0][x][y]=="#":   #if there is a ship it will be struck
                player2_board[0][x][y]="!"         #this can be seen on both tables
                player2emptyboard[0][x][y]="!"
                print_hit()
                continue


            #changes should be seen on both tables

            if player2_board[0][x][y]=="-":
                player2_board[0][x][y]="O"
                player2emptyboard[0][x][y]="O"
                print_miss()
                while True:
                    print_type_done_to_yield(2)
                    done=input().lower()
                    if done=="done":
                        break

                turn+=1
        #same code for player 2
        if turn % 2 == 0:
            print_3d_list(player1emptyboard+player2_board)
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            strikecoordinats = input().split()
            strikecoordinats = strikecoordinats[0:2]

            if len(strikecoordinats)!=2:
                print_incorrect_input_format()
                continue


            try:
                int(strikecoordinats[0])
                int(strikecoordinats[1])
            except:
                print_incorrect_input_format()
                continue


            if strikecoordinats[0] not in ["{}".format(i) for i in range(1, 11)] or strikecoordinats[1] not in ["{}".format(i) for i in range(1, 11)]:
                print_incorrect_coordinates()
                continue


            y = int(strikecoordinats[0])-1
            x = int(strikecoordinats[1])-1

            if player1emptyboard[0][x][y] in ["!", "O"]:
                print_tile_already_struck()
                continue

            if player1_board[0][x][y] == "#":
                player1_board[0][x][y] = "!"
                player1emptyboard[0][x][y] = "!"
                print_hit()
                continue


            if player1_board[0][x][y] == "-":
                player1_board[0][x][y] = "O"
                player1emptyboard[0][x][y] = "O"
                print_miss()
                while True:
                    print_type_done_to_yield(1)
                    done = input().lower()
                    if done == "done":
                        break

                turn += 1

































        # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

