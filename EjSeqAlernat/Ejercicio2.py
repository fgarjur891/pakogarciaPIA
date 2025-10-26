#  2. Calcular el perí­metro y área de un rectángulo dada su base y su altura.
base = int(input('Dime la base del rectángulo '))
altura = int(input('Dime la altura '))
area_rect = base * altura
perim = 2 * (base + altura)
print ("El area es " , area_rect)
print ("El perímetro es " , perim)
