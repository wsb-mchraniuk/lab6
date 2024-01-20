#!/usr/bin/env python3
import sys

if len(sys.argv) != 4:
    print("Uzycie: calc.py <liczba_1> <+ lub -> <liczba_2>")
    sys.exit(1)


liczba1, operacja, liczba2 = float(sys.argv[1]), sys.argv[2], float(sys.argv[3])

if operacja == '+':
    wynik = liczba1 + liczba2
elif operacja == '-':
    wynik = liczba1 - liczba2
else:
    print("Niewłaściwa operacja. Wprowadź + lub -.")
    sys.exit(1)

with open("/tmp/wynik.txt", "w") as plik_wynikowy:
    plik_wynikowy.write(str(wynik))

print("Wynik: %.2f" % wynik)
