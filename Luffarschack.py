import os

# Funktion för att skapa spelbrädet
def visa_spelplan(spelplan):
    for rad in spelplan:
        print(" | ".join(rad))
        print("-" * 9)

# Funktion för att ta emot spelarinput
def spelar_input(spelplan, tur):
    while True:
        try:
            val = int(input("Spelare {}: Välj en position (1-9): ".format(tur)))
            row = (val - 1) // 3
            col = (val - 1) % 3
            if val < 1 or val > 9 or spelplan[row][col] != " ":
                raise ValueError
            return row, col
        except ValueError:
            print("Ogiltigt val. Försök igen.")

# Funktion för att kolla vinnare
def kolla_vinnare(spelplan):
    for rad in spelplan:
        if rad.count(rad[0]) == 3 and rad[0] != " ":
            return rad[0]
    for col in range(3):
        if spelplan[0][col] == spelplan[1][col] == spelplan[2][col] and spelplan[0][col] != " ":
            return spelplan[0][col]
    if spelplan[0][0] == spelplan[1][1] == spelplan[2][2] and spelplan[0][0] != " ":
        return spelplan[0][0]
    if spelplan[0][2] == spelplan[1][1] == spelplan[2][0] and spelplan[0][2] != " ":
        return spelplan[0][2]
    return None

# Funktion för att spara statistik
def spara_statistik(vinnare, antal_drag):
    filnamn = "spelstatistik.txt"
    if os.path.exists(filnamn):
        with open(filnamn, "r") as fil:
            statistik = fil.readlines()
            statistik = [line.strip().split(":") for line in statistik]
            statistik = {line[0]: int(line[1]) for line in statistik}
    else:
        statistik = {"Spelade spel": 0, "X_vinster": 0, "O_vinster": 0, "Oavgjorda": 0, "Totala_drag": 0}

    statistik["Spelade spel"] += 1
    statistik["Totala_drag"] += antal_drag
    if vinnare == "X":
        statistik["X_vinster"] += 1
    elif vinnare == "O":
        statistik["O_vinster"] += 1
    else:
        statistik["Oavgjorda"] += 1

    with open(filnamn, "w") as fil:
        for key, value in statistik.items():
            fil.write(f"{key}:{value}\n")

# Huvudfunktion för spelet
def luffarschack():
    spelplan = [[" " for _ in range(3)] for _ in range(3)]
    tur = "X"
    drag = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        visa_spelplan(spelplan)
        row, col = spelar_input(spelplan, tur)

        spelplan[row][col] = tur
        drag += 1

        vinnare = kolla_vinnare(spelplan)
        if vinnare:
            os.system("cls" if os.name == "nt" else "clear")
            visa_spelplan(spelplan)
            print("Spelare", vinnare, "vinner!")
            spara_statistik(vinnare, drag)
            break
        elif drag == 9:
            os.system("cls" if os.name == "nt" else "clear")
            visa_spelplan(spelplan)
            print("Oavgjort!")
            spara_statistik(None, drag)
            break

        tur = "O" if tur == "X" else "X"

if __name__ == "__main__":
    luffarschack()