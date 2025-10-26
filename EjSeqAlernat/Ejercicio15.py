# 15. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
# después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

moneda2e = int(input("Monedas 2€"))
moneda1e = int(input("Monedas 1€"))
moneda50cs = int(input("Monedas 0,50€"))
moneda20cs = int(input("Monedas 0,20€"))
moneda10cs = int(input("Monedas 0,10€"))

totaleu = float(moneda2e * 2 + moneda1e * 1 + moneda50cs * 0.50 + moneda20cs * 0.20 + 
                    moneda10cs * 0.10)
print("Total: ",int(totaleu), "Euros",int((totaleu - int(totaleu))*100), "centimos")

