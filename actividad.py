#Punto 1

titulo1 ="punto 1"
print(titulo1.center(20, "_"))
name ="Luis"
age=27
favouriteFood="Pasta con salsa Boloñesa"
presentacion=f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print(presentacion)

#Punto 2
titulo2 ="punto 2"
print(titulo2.center(20, "_"))
fullName = "Luis alfonso Vejarano"
contarNombre= len(fullName.replace(" ", "")) #quita los espacios y cuneta las letras
print(f"Hola, {fullName}! Tu nombre tiene {contarNombre} letras.")

# Mostrar el mensaje
titulo3 ="punto 3"
print(titulo3.center(20, "_"))

#punto 3
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
print(f"Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}% y los ingresos crecieron un {revenueGrowthPercent:.2f}%.")

titulo4 ="punto 4"
print(titulo4.center(20, "_"))
secretMessage = "aS!Ir waQm VL!eDafrcnXi n=gS .P,yytahgoln.!"
omitoCaracteres=secretMessage[3:]   #omito los 3 primeros caracters
indices=[0, 2, 4, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

omitoCaracteres= ''.join(omitoCaracteres[i]for i in indices)   #recorro la lista sacando solo el indice y luego lo uno sin espacios
print(omitoCaracteres)

titulo5 ="punto 5"
print(titulo5.center(20, "_"))
text = "El nombre 'Python' viene dado por la afición de Van Rossum al grupo Monty Python."
numero_de_palabras = len(text.split())   #separa y cuenta las palabras 
print(f"Numero de palabras en la frase: {numero_de_palabras}")

titulo6 ="punto 6"
print(titulo6.center(20, "_"))
word ="Camila "
new_word = word.replace('a', 'e')
print(new_word)
titulo7 ="punto 7"
print(titulo7.center(20, "_"))
sentence = "La historia del lenguaje de programación Python"
words = sentence.split()
reversed_sentence = ' '.join(reversed(words))
print(reversed_sentence)


