import random         # Sadece aynı harfi random tekrar seçebiliyor, o kısım problemse üzerinde çalışılabilir.
name = input("Enter your fullname without spaces :").lower().replace(" ","")
print(name)
s = len(name)-1
for i in range(3):
    print(name[random.randint(0,s)], end= "")
for x in range(4):
    print(random.randint(0,9), end="")