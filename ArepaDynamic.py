#Establecemos las medidas de los ingredientes
Taza = 1 
Cucharada = Taza/16
Cucharadita= Cucharada/3

#Pedimos la cantidad de tazas, cucharadas y cucharaditas para las arepas
Harina = float(input("Cuantas Tazas de Harina"))
Agua = float(input("Cuantas Tazas de Agua"))
Aceite = float(input("Cuantas Cucharadas de Aceite"))
Sal = float(input("Cuantas Cucharaditas de Sal"))

#Calculamos la cantidad de productos de los ingredientes a usar
HarinaUsar = Harina * Taza
AguaUsar = Agua * Taza
AceiteUsar = Aceite * Cucharada
SalUsar = Sal * Cucharadita

#Sumamos todos los ingredientes
CantidadIngredientes = HarinaUsar + AguaUsar + AceiteUsar + SalUsar
print("La cantidad de ingredientes es: "+str(CantidadIngredientes)+" Tazas")


Arepa = 4 #cantidad de ingrediente necesario para una arepa

#Calculamos la cantidad de arepas que podemos hacer
CantidadArepa = CantidadIngredientes / Arepa
print("La cantidad de arepas que podemos hacer es: "+str(CantidadArepa)+" Arepas")