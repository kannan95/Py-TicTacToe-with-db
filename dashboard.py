print('''
                    WELCOME TO TIC TAC TOE 
                      PLAYER VS PLAYER
''')

def username_check(number):
    import re
    while True:
        try:
            player = str(input("Enter Player{} name : ".format(number)))
            if(re.search('\W', player)):
                print("Wrong Input")
            else:
                return player
        except:
            print("Please, Dont leave player name blank!")


def main_function():
    from sql import show_database,reset_table

    option_check = True
    while option_check:
        option = str(input("Choose the option:\n1.Type P to play\n2.Type L to leaderboard\n3.Type R to reset the leaderboard\n4.Type E to exit\n>>>"))
        if (option.lower() != 'p' and option.lower() != 'l' and option.lower() != 'e'and option.lower() != 'r'):
            print("Wrong option")
        else:
            option_check = False
    while True:
        if option.lower() == 'p':
            from TTT import ttt_main
            ttt_main()
        elif option.lower() == 'l':
            show_database()
            main_function()
        elif option.lower() == 'r':
            reset_table()
            main_function()
        elif option.lower() == 'e':
            exit(1)

u_check = True
while u_check:
    player1 = username_check(1)
    player2 = username_check(2)
    if player1 != player2:
        u_check = False
    else:
        print("Player\'s name should not be same!")
main_function()

if __name__ == '__main__':

    main_function()
