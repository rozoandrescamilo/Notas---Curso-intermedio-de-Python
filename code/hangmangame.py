import random
import os


def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s


def read_data(filepath="./words.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = read_data(filepath="./words.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    lifes = 7

    while True:
        os.system("cls")
        print("Recuerda: Tienes " + str(lifes) +" vidas. Ten cuidado.")
        print("""
         ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''./
        | |/         |/  _  \/
        | |          ||  `/,|
        | |          (\.`_.'
        | |         .-`--'.
        | |        /Y . . Y\.
        | |       // |   | \..
        | |      //  | . |  \..
        | |     ()   |   |   ()
        | |          ||'||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \.
-------------------------
|  -------------------- |
| |                   | |
: :                   : :
-------------------------
|  ¡ADIVINA LA PALABRA!  |
""")

        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")


        try:
            letter = input("Ingresa una letra y presiona Enter: ").strip().upper()
            assert letter.isalpha(), input("¡SOLO PUEDES INGRESAR LETRAS!, Presiona la tecla Enter para continuar.")
            assert len(letter) == 1, input("¡SOLO UNA LETRA POR FAVOR!, Presiona la tecla Enter para continuar.")
        except AssertionError as e:
            print(e)
            continue


        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        else:
            lifes -= 1
            if lifes == -1:
                os.system("cls")

                lose = input("""
                    ⠄⢀⣀⣤⣴⣶⣶⣤⣄⡀⠄⠄⣀⣤⣤⣤⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣴⣏⣹⣿⠿⠿⠿⠿⢿⣿⣄⢿⣿⣿⣿⣿⣿⣋⣷⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣿⢟⣩⣶⣾⣿⣿⣿⣶⣮⣭⡂⢛⣭⣭⣭⣭⣭⣍⣛⣂⡀⠄⠄⠄⠄⠄⠄⠄⠄
                    ⣿⣿⣿⣿⡿⢟⣫⣭⣷⣶⣾⣭⣼⡻⢛⣛⣭⣭⣶⣶⣬⣭⣅⡀⠄⠄⠄⠄⠄⠄
                    ⣿⡿⢏⣵⣾⣿⣿⣿⡿⢉⡉⠙⢿⣇⢻⣿⣿⣿⣿⡟⠉⠉⢻⡷⠄⠄⠄⠄⠄⠄
                    ⣿⣷⣾⣍⣛⢿⣿⣿⣿⣤⣁⣤⣿⢏⠸⣿⣿⣿⣿⣷⣬⣥⣾⠁⣿⣿⣷⠄⠄⠄
                    ⣿⣿⣿⣿⣭⣕⣒⠿⠭⠭⠭⡷⢖⣫⣶⣶⣬⣭⣭⣭⣭⣥⡶⢣⣿⣿⣿⠄⠄⠄
                    ⣿⣿⣿⣿⣿⣿⣿⡿⣟⣛⣭⣾⣿⣿⣿⣝⡛⣿⢟⣛⣛⣁⣀⣸⣿⣿⣿⣀⣀⣀
                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                    ⣿⡿⢛⣛⣛⣛⣙⣛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣭⣭⠽⣛⢻⣿⣿⣿⠛⠛⠛
                    ⣿⢰⣿⣿⣿⣿⣟⣛⣛⣶⠶⠶⠶⣦⣭⣭⣭⣭⣶⡶⠶⣾⠟⢸⣿⣿⣿⠄⠄⠄
                    ⡻⢮⣭⣭⣭⣭⣉⣛⣛⡻⠿⠿⠷⠶⠶⠶⠶⣶⣶⣾⣿⠟⢣⣬⣛⡻⢱⣇⠄⠄
                    ⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠶⠒⠄⠄⠄⢸⣿⢟⣫⡥⡆⠄⠄
                    ⢭⣭⣝⣛⣛⣛⣛⣛⣛⣛⣿⣿⡿⢛⣋⡉⠁⠄⠄⠄⠄⠄⢸⣿⢸⣿⣧⡅⠄⠄
                    ⣶⣶⣶⣭⣭⣭⣭⣭⣭⣵⣶⣶⣶⣿⣿⣿⣦⡀⠄⠄⠄⠄⠈⠡⣿⣿⡯⠁⠄⠄
`7MMMMMMq.`7MMMMMYMM  `7MMMMMMMq.  `7MMMMMYb.`7MMF' .MMMMbgd MMP""MM""YMM `7MMMMMYMM
  MM   `MM. MM    `7    MM   `MM.   MM    `Yb. MM  ,MI    "Y P'   MM   `7   MM    `7
  MM   ,M9  MM   d      MM   ,M9    MM     `Mb MM  `MMb.          MM        MM   d
  MMmmdM9   MMmmMM      MMmmdM9     MM      MM MM    `YMMNq.      MM        MMmmMM
  MM        MM   Y  ,   MM  YM.     MM     ,MP MM  .     `MM      MM        MM   Y  ,
  MM        MM     ,M   MM   `Mb.   MM    ,dP' MM  Mb     dM      MM        MM     ,M
.JMML.    .JMMmmmmMMM .JMML. .JMM..JMMmmmdP' .JMML.P"Ybmmd"     .JMML.    .JMMmmmmMMM
_____________________________________________________________________________________
Presiona la tecla (X) para jugar otra vez, ó presiona cualquier otra tecla para salir\n""").upper()
                if lose == "X":
                    lifes = 7
                    chosen_word = random.choice(data)
                    chosen_word_list = [letter for letter in chosen_word]
                    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
                    letter_index_dict = {}
                    for idx, letter in enumerate(chosen_word):
                        if not letter_index_dict.get(letter):
                            letter_index_dict[letter] = []
                        letter_index_dict[letter].append(idx)
                    continue
                else:
                    break



        if "_" not in chosen_word_list_underscores:
            os.system("cls")
            print("""
                            ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
                            ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
                            ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀
                            ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
                            ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
                             ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
   .g8MMMbgd       db      `7MN.   `7MF'    db       .MMMMbgd MMP""MM""YMM `7MMMMMYMM
.dP'     `M      ;MM:       MMN.    M      ;MM:     ,MI    "Y P'   MM   `7   MM    `7
dM'       `     ,V^MM.      M YMb   M     ,V^MM.    `MMb.          MM        MM   d
MM             ,M  `MM      M  `MN. M    ,M  `MM      `YMMNq.      MM        MMmmMM
MM.    `7MMF'  AbmmmqMA     M   `MM.M    AbmmmqMA   .     `MM      MM        MM   Y  ,
`Mb.     MM   A'     VML    M     YMM   A'     VML  Mb     dM      MM        MM     ,M
  `"bmmmdPY .AMA.   .AMMA..JML.    YM .AMA.   .AMMA.P"Ybmmd"     .JMML.    .JMMmmmmMMM
---------------------------------------------------------------------------------------""")
            print("¡Felicitaciones! Lo lograste. La palabra era: ", chosen_word)
            choice = input("Presiona la tecla (X) para jugar otra vez, ó presiona cualquier otra tecla para salir\n").upper()
            if choice == "X":
                lifes = 7
                chosen_word = random.choice(data)
                chosen_word_list = [letter for letter in chosen_word]
                chosen_word_list_underscores = ["_"] * len(chosen_word_list)
                letter_index_dict = {}
                for idx, letter in enumerate(chosen_word):
                    if not letter_index_dict.get(letter):
                        letter_index_dict[letter] = []
                    letter_index_dict[letter].append(idx)
                continue
            else:
                break


menu = """
_______________________________________________________________
888
888
888
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b
888  888.d888888888  888888  888888  888  888.d888888888  888
888  888888  888888  888Y88b 888888  888  888888  888888  888
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888
                             888
                        Y8b d88P
                         "Y88P"
---------------------------------------------------------------
                         |/|
                         |/| /¯)
                         |/|/\/
                         |/|\/
                        (¯¯¯)
                        (¯¯¯)
                        (¯¯¯)
                        (¯¯¯)
                        /¯¯/\.
                       / ,^./\.
                      / /   \/\.
                     / /     \/\.
                    ( (       )/)
                    | |       |/|
                    | |       |/|
                    ( (       )/)
                     \ \     / /
                      \ `---' /
                       `-----'
______________________________________________________________
|     BIENVENIDO AL JUEGO DEL AHORACADO Ó HANGMAN GAME        |
--------------------------------------------------------------
Para comenzar presiona (1) y luego (Enter)
Para salir presiona (Ctrl + C)
______________________________________________________________
"""


while True:
    try:
        opcion = input(menu)
        if int(opcion) == 1:
            run()
        else: input("Debes ingresar el número 1 para jugar. Presiona la tecla Enter para reintentar.")
        assert len(str(opcion)) == 1, input("¡No puedes ingresar varias letras o números!, Presiona la tecla Enter para reintentar.")
    except AssertionError as a:
        print(a)
    except ValueError:
        input("No se aceptan letras, ingresa el número 1 para jugar. Presiona la tecla Enter para reintentar.")


if __name__ == '__main__':
    run()