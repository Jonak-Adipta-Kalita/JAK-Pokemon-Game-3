choose_a = ["A", "a"]
choose_b = ["B", "b"]
choose_c = ["C", "c"]
choose_d = ["D", "d"]
choose_e = ["E", "e"]
choose_f = ["F", "f"]
choose_g = ["G", "g"]
choose_h = ["H", "h"]

def region():
    print("A) Kanto")
    print("B) Jhoto")
    print("C) Hoenn")
    print("D) Sinnoh")
    print("E) Unova")
    print("F) Kalos")
    print("G) Alola")
    print("H) Galar")

def Kanto():
    print("A) Charmender")
    print("B) Bulbasaur")
    print("C) Squirtle")
    choose = input(">> ")
    print()
    if choose in choose_a:
        print("You choosed Charmender")
    elif choose in choose_b:
        print("You choosed Bulbasaur")
    elif choose in choose_c:
        print("You choosed Squirtle")
    else:
        print("Error")
        print("Choose again!!")
        Kanto()

def Jhoto():
    print("A) Cyndaquil")
    print("B) Chikorita")
    print("C) Totodile")
    choose = input(">> ")
    print()
    if choose in choose_a:
        print("You choosed Cyndaquil")
    elif choose in choose_b:
        print("You choosed Chikorita")
    elif choose in choose_c:
        print("You choosed Totodile")
    else:
        print("Error")
        print("Choose again!!")
        Jhoto()

def Hoenn():
    print("A) Torchic")
    print("B) Treeko")
    print("C) Mudkip")
    choose = input(">> ")
    print()
    if choose in choose_a:
        print("You choosed Torchic")
    elif choose in choose_b:
        print("You choosed Treeko")
    elif choose in choose_c:
        print("You choosed Mudkip")
    else:
        print("Error")
        print("Choose again!!")
        Hoenn()

def Sinnoh():
    print("A) Chimchar")
    print("B) Turtwig")
    print("C) Piplup")
    choose = input(">> ")
    print()
    if choose in choose_a:
        print("You choosed Chimchar")
    elif choose in choose_b:
        print("You choosed Turtwig")
    elif choose in choose_c:
        print("You choosed Piplup")
    else:
        print("Error")
        print("Choose again!!")
        Sinnoh()

def Unova():
    print("A) Tepig")
    print("B) Snivy")
    print("C) Oshawott")
    choose = input(">> ")
    print()
    if choose in choose_a:
        print("You choosed Tepig")
    elif choose in choose_b:
        print("You choosed Snivy")
    elif choose in choose_c:
        print("You choosed Oshawott")
    else:
        print("Error")
        print("Choose again!!")
        Unova()

def Kalos():
    print("A) Fennekin")
    print("B) Chespin")
    print("C) Froakie")
    choose = input(">> ")
    print()
    if choose in choose_a:
        print("You choosed Fennekin")
    elif choose in choose_b:
        print("You choosed Chespin")
    elif choose in choose_c:
        print("You choosed Froakie")
    else:
        print("Error")
        print("Choose again!!")
        Kalos()

def Alola():
    print("A) Litten")
    print("B) Rowlet")
    print("C) Popplio")
    choose = input(">> ")
    print()
    if choose in choose_a:
        print("You choosed Litten")
    elif choose in choose_b:
        print("You choosed Rowlet")
    elif choose in choose_c:
        print("You choosed Popplio")
    else:
        print("Error")
        print("Choose again!!")
        Alola()

def Galar():
    print("A) Scorbunny")
    print("B) Grookey")
    print("C) Sobble")
    choose = input(">> ")
    print()
    if choose in choose_a:
        print("You choosed Scorbunny")
    elif choose in choose_b:
        print("You choosed Grookey")
    elif choose in choose_c:
        print("You choosed Sobble")
    else:
        print("Error")
        print("Choose again!!")
        Galar()

def main():
    print("$"*10, "WELCOME TO JAK Pokemon Game", "$"*10)
    print(" ")
    print("$"*14, "Choose You Starter", "$"*15)
    print(" ")
    print(" ")
    print("Which region you want to go with??")
    print()
    region()
    choose = input(">> ")
    print()
    if choose in choose_a:
        Kanto()
    elif choose in choose_b:
        Jhoto()
    elif choose in choose_c:
        Hoenn()
    elif choose in choose_d:
        Sinnoh()
    elif choose in choose_e:
        Unova()
    elif choose in choose_f:
        Kalos()
    elif choose in choose_g:
        Alola()
    elif choose in choose_h:
        Galar()
    else:
        print("Choose a valid Region")
        region()

main()
