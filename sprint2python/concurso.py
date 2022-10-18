print(" ")
print("Responde con el corazón pero no olvides la cabeza :)")
print("Quien gano el mundial de corea 2002?")
print("a) Alemania ")
print("b) Turquía")
print("c) Brasil")

respuesta =""
cont=0

respuesta = input("Elige una de las opciones(a,b,c): ")

while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
    respuesta = input ("Elige una de las respuestas(a,b,c): ")
            
if respuesta =="c":
    print("Tenemos a un nuevo genio")
    cont=cont + 10
else:
    print("Era demasiado fácil , como lo has fallado")
    cont=cont - 5

print(" ")
print("Responde con el corazón pero no olvides la cabeza :)")
print("Quien gano la champions en 2014?")
print("a) Brujas ")
print("b) Bayern Munich")
print("c) Real Madrid")

respuesta =""

respuesta = input("Elige una de las opciones(a,b,c): ")

while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
    respuesta = input ("Elige una de las respuestas(a,b,c): ")
            
if respuesta =="c":
    print("Tenemos a un nuevo genio")
    cont=cont + 10
else:
    print("Era demasiado fácil , como lo has fallado")
    cont=cont - 5

print(" ")
print("Responde con el corazón pero no olvides la cabeza :)")
print("Quien gano la premier league en 2016?")
print("a) Man City ")
print("b) Leicester")
print("c) Liverpool")

respuesta =""

respuesta = input("Elige una de las opciones(a,b,c): ")

while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
    respuesta = input ("Elige una de las respuestas(a,b,c): ")
            
if respuesta =="b":
    print("Tenemos a un nuevo genio")
    cont=cont + 10
else:
    print("Era demasiado fácil , como lo has fallado")
    cont=cont - 5

print("La puntuación que has conseguido es de:"+str(cont))
