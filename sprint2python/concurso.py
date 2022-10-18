print(" ")
print("Responde con el corazón pero no olvides la cabeza :)")
print("Quien gano el mundial de corea 2002?")
print("a) Alemania ")
print("b) Turquía")
print("c) Brasil")

respuesta =""

respuesta = input("Elige una de las opciones(a,b,c): ")

while(respuesta !="a" and respuesta !="b" and respuesta !="c" ):
    respuesta = input ("Elige una de las respuestas(a,b,c): ")
    
if respuesta =="c":
    print("Tenemos a un nuevo genio")
else:
    print("Era demasiado fácil , como lo has fallado")
