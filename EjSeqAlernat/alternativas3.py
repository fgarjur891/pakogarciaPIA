# Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. 
# Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

edad1 = int(input("Dime la edad de una persona: "))
edad2 = int(input("Dime la segunda edad: "))

if edad1 < edad2:
    print("La primera persona es menor")
elif edad1 > edad2:
    print("La segunda persona es menor")
else:
    print("Tienen idéntica edad")

