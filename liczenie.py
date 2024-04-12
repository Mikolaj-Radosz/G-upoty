import random
def gra_w_karty():
    print ('Gra w karty')
    talia_wzor = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                  '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    talia = list(talia_wzor.keys())*4
    random.shuffle(talia)
    print (talia)
    talia_gracz1 = []
    talia_gracz2 = []
    for i in range(26):
        talia_gracz1.append(talia.pop())
        talia_gracz2.append(talia.pop())
    print (talia_gracz1)
    print (talia_gracz2)


def walka_wojownikow():
    wojownik1 = random.randint(1, 10)
    wojownik2 = random.randint(1, 10)
    wojownik1_wynik = 0
    wojownik2_wynik = 0
    for i in range(10):
        i = i+1
        print (f'runda: {i}')
        if wojownik1 > wojownik2:
            print ('Wojownik 1 wygrywa')
            wojownik1_wynik = wojownik1_wynik + 1

        else:
            print ('Wojownik 2 wygrywa')
            wojownik2_wynik = wojownik2_wynik + 1
        wojownik1 = random.randint(1, 10)
        wojownik2 = random.randint(1, 10)
        if i == 10:
            print ('Gotowe')
            if wojownik1_wynik > wojownik2_wynik:
                print ('Całą walkę wygrywa wojownik 1')
            else:
                print ('Całą walkę wygrywa wojownik 2')
            

    print ('Bardzo lubię')


print ("""Witaj w moim programie. Wybierz konkretny program:
       1. Gra w karty
       2. Walka wojowników
       3. Koniec programu""")
tomba_bomba = True
while tomba_bomba:
    wstep = input('Wybierz program: ')
    if wstep == '1':
        gra_w_karty()
    elif wstep == '2':
        walka_wojownikow()
    elif wstep == '3':
        print ('Koniec programu')
        tomba_bomba = False
    


    