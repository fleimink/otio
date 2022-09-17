import math

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
            ir = int(I) * int(R)
            print(ir)
    elif R == "0":
        if I == "0":
            print("Oops")
        else:
            pi = int(P) / int(I)
            print(pi)
    elif I == "0":
        if P == "0":
            print("Oops.")
        else:
            pr = math.sqrt(int(P) * int(R))
            print(pr)
            
def current():
    if U == "0":
        if R == "0":
            print("Oops")
        else:
            pdelr = math.sqrt(int(P) / int(R))
            print(pdelr)
    elif R == "0":
        if P == "0":
            print("Oops")
        else:
            pu = int(P) / int(U)
            print(pu)
    elif P == "0":
        if U == "0":
            print("Oops")
        else:
            ur = int(U) / int(R)
            print(ur)
def power():
    if U == "0":
        if I == "0":
            print("Oops")
        else:
            i2r = (int(I) * int(I)) * int(R)
            print(i2r)
    elif I == "0":
        if U == "0":
            print("Oops")
        else:
            u2r = (int(U) * int(U)) / int(R)
            print(u2r)
    elif R == "0":
        if I == "0":
            print("Oops")
        else:
            Ui = int(U) * int(I)
            print(Ui)
def resistance():
    if P == "0":
        if I == "0":
            print("Oops")
        else:
            uidel = int(U) / int(I)
            print(uidel)
    elif U == "0":
        if P == "0":
            print("Oops")
        else:
            pi2 = int(P) / (int(I) * int(I))
            print(pi2)
    elif I == "0":
        if P == "0":
            print("Oops")
        else:
            u2p = (int(U) * int(U)) / int(P)
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