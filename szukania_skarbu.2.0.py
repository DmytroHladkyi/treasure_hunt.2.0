from math import sqrt
from random import randint

game_width = int(input("Podaj szerokość (X): "))
game_hight = int(input("Podaj wysokość (Y): "))

key_x = randint(0, game_width)
key_y = randint(0, game_hight)
player_x = randint(0, game_width)
player_y = randint(0, game_hight)
player_found_key = False
tries = 0

distance_befor = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
# print("pozycja skarbu", key_x,key_y)
print("pozycja gracza", player_x, "X",player_y, "Y")

while not player_found_key:
    tries += 1
    print()
    move_x = int(input("Podaj oś x. "))
    move_y = int(input("Podaj oś y. "))
    
    if move_x != key_x or move_y != key_y:
        print("Próbuj dalej")
        
    if move_x > game_width or move_y > game_hight:
        print("Wychodzisz poza pole!")
        continue
    if move_x == key_x and move_y == key_y:
        print("Bravo! Znalazłeść skarb!")
        print(f'Podjąłeś {tries} prób. Skarb znajdował się w {key_x}(X)/{key_y}(Y)')
        quit()   
        
    distance_after = sqrt((key_x - move_x) ** 2 + (key_y - move_y) ** 2)

    if distance_befor > distance_after:
        print("Cieplej.")
    else:
        print("Zimniej.")

    distance_befor = distance_after
    print("Twoja próba: ", move_x,move_y)