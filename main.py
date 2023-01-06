import math
from pyfiglet import Figlet

f = Figlet(font='slant')

print(f.renderText("O T I O"))

born = """
Найти напряжение/Find voltage(Volts) = 1
Найти силу тока/Find current strength(Amps) = 2
Найти мощность/Find power(Watt or Power) = 3
Найти сопротивление/Find resistance(Ohms) = 4
"""
print(born)
chuice = input(": ")

print("Если нет значение, пишите 0/If there is no value, write 0")
U = input("Напряжение/voltage(U or V): ")
I = input("Сила тока/current strength(I): ")
P = input("Мощность/power(P): ")
R = input("Сопротивление/resistance(R): ")

def voltage():  
    if P == "0":
        if R == "0":
            print("Opps")
        else:
            ir = float(I) * float(R)
            print(ir)
    elif R == "0":
        if I == "0":
            print("Oops")
        else:
            pi = float(P) / float(I)
            print(pi)
    elif I == "0":
        if P == "0":
            print("Oops.")
        else:
            num11 = math.sqrt(float(P))
            num21 = math.sqrt(float(R))
            num31 = num11 * num21
            #pr = math.sqrt(float(P) * float(R))
            print(num31)
            
def current():
    if U == "0":
        if R == "0":
            print("Oops")
        else:
            num12 = math.sqrt(float(P))
            num22 = math.sqrt(float(R))
            num32 = num12 / num22
            #pdelr = math.sqrt(float(P) / float(R))
            print(num32)
    elif R == "0":
        if P == "0":
            print("Oops")
        else:
            pu = float(P) / float(U)
            print(pu)
    elif P == "0":
        if U == "0":
            print("Oops")
        else:
            ur = float(U) / float(R)
            print(ur)
def power():
    if U == "0":
        if I == "0":
            print("Oops")
        else:
            i2r = (float(I) * float(I)) * float(R)
            print(i2r)
    elif I == "0":
        if U == "0":
            print("Oops")
        else:
            u2r = (float(U) * float(U)) / float(R)
            print(u2r)
    elif R == "0":
        if I == "0":
            print("Oops")
        else:
            Ui = float(U) * float(I)
            print(Ui)
def resistance():
    if P == "0":
        if I == "0":
            print("Oops")
        else:
            uidel = float(U) / float(I)
            print(uidel)
    elif U == "0":
        if P == "0":
            print("Oops")
        else:
            pi2 = float(P) / (float(I) * float(I))
            print(pi2)
    elif I == "0":
        if P == "0":
            print("Oops")
        else:
            u2p = (float(U) * float(U)) / float(P)
            print(u2p)
        

def Main():
    if chuice == "1":
        voltage()
    if chuice == "2":
        current()
    if chuice == "3":
        power()
    if chuice == "4":
        resistance()

if __name__ == "__main__":
    Main()
#
