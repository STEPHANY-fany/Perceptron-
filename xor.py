#xor es para la desigualdad, da verdadero cuando las  entradas no son iguales
matriz = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

w1 = 0.01
w2 = 0.01
b = 0.0
taza_de_aprendizaje = 0.1
epoca = 0
aprendido = 0

while aprendido !=20:
    errores = 0 
    print("Época:", epoca + 1 ,end=' ')
    for fila in matriz:
        x1, x2, d = fila   

        
        z = (w1 * x1) + (w2 * x2) + b
        y = 1 if z >= 0 else 0

        print ("x1=",x1,"x2=",x2,"d=",d,"y=",y)

        
        if y != d: 
            errores += 1
            
            w1 = w1 + taza_de_aprendizaje * (d - y) * x1
            w2 = w2 + taza_de_aprendizaje * (d - y) * x2
            b = b + taza_de_aprendizaje * (d - y)
            print("Error, actualizando pesos....")
            print("Valores actualizados  w1=",w1,"w2=",w2,"b=",b)
        

    
    if errores == 0:
        aprendido==0
    else:
        epoca += 1 
        aprendido +=1
