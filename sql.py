import sqlite3 as sql
from TTT import *
from dashboard import *
from prettytable import PrettyTable

database = sql.connect('TicTacToe.db')
cur = database.cursor()


def creating_table():

    # cur.execute('DROP TABLE IF EXISTS TTT_tbl;')
    database.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS TTT_tbl'
                '(ID INTEGER NOT NULL PRIMARY KEY,NAME text, WIN INT DEFAULT 0,LOSS INT DEFAULT 0, DRAW INT DEFAULT 0 );')
    database.commit()


def inserting_into_db():
    fetch_p1 = list(cur.execute('SELECT WIN, LOSS, DRAW FROM TTT_tbl WHERE NAME = ?;', (player1,)))
    values_p1 = [i for a in fetch_p1 for i in a]
    fetch_p2 = list(cur.execute('SELECT WIN, LOSS, DRAW FROM TTT_tbl WHERE NAME = ?;', (player2,)))
    values_p2 = [i for a in fetch_p2 for i in a]
    check_player = list(cur.execute("SELECT NAME FROM TTT_tbl;"))
    final_input = [i for a in check_player for i in a]
    database.commit()

    if  values_p1:
        list1 = [a + b for a, b in zip(values_p1, player1_values)]
    else:
        list1 = player1_values
    if  values_p2:
        list2 = [a + b for a, b in zip(values_p2, player2_values)]
    else:
        list2 = player2_values

    if player1 not in final_input:
        cur.execute('''Insert into TTT_tbl(NAME,WIN,LOSS,DRAW) Values(?, ?,?,?);''',
                    (player1, list1[0], list1[1], list1[2]))
        database.commit()
    else:
        cur.execute('''UPDATE TTT_tbl SET WIN = ? , LOSS = ? , DRAW = ? WHERE NAME = ?;''',
                    (list1[0], list1[1], list1[2], player1))
        database.commit()
    if player2 not in final_input:
        cur.execute('''Insert into TTT_tbl(NAME,WIN,LOSS,DRAW) Values(?, ?,?,?);''',
                    (player2, list2[0], list2[1], list2[2]))
        database.commit()
    else:
        cur.execute('''UPDATE TTT_tbl SET WIN = ? , LOSS = ? , DRAW = ? WHERE NAME = ?;''',
                    (list2[0], list2[1], list2[2], player2))
        database.commit()


def show_database():
    p_db = list(cur.execute("SELECT * FROM TTT_tbl;"))
    table = PrettyTable(['ID', 'Name', 'Win', 'Loss', 'Draw'])
    table.align["Name"] = "l"  # Left align city names
    table.padding_width = 1
    for i in p_db:
        table.add_row(i)
    print(table)

def reset_table():
    cur.execute('DELETE FROM TTT_tbl')
    database.commit()
    print('Reset done.')

def sql_main():
    creating_table()
    inserting_into_db()
    import dashboard
    dashboard.main_function()
    cur.close()
    database.close()


if __name__ == "__main__":
    sql_main()

