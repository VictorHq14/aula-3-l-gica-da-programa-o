mult = 0
num = int(input("Digite um número aleatório:  "))

while mult < 10:
    mult += 1
    multiplicação = num * mult
    if multiplicação % 3 == 0 :
        print(f"{num} x {mult} = {multiplicação} que é divisivel por 3")
