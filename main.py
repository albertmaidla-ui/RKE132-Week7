import datetime
from functions import say_hello, greet_user, add

# Praegune kuupäev ja kellaaeg
now = datetime.datetime.now()

print("Aasta:", now.year)
print("Kuu:", now.month)
print("Päev:", now.day)
print("Tund:", now.hour)
print("Minut:", now.minute)
print("Sekund:", now.second)

# Kuupäeva ja kellaaja vormindamine
print("Kuupäev:", now.strftime("%d.%m.%Y"))
print("Nädalapäev ja kuu:", now.strftime("%A, %d %B %Y"))
print("Kellaaeg:", now.strftime("%H:%M"))
print("Kellaaeg 12 tunni vormis:", now.strftime("%I:%M %p"))

# Funktsioonide kasutamine
say_hello()

name = input("Sisesta oma nimi: ")
greet_user(name)

result = add(5, 3)
print("Arvude 5 ja 3 summa:", result)