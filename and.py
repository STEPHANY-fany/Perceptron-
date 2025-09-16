#poner solo 2 decimales 
matriz = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

w1 = 0.0
w2 = 0.0
b = 0.0
taza_de_aprendizaje = 0.1
epoca = 0
aprendido = False

while not aprendido:
    errores = 0
    print("\nÉpoca:", epoca + 1)
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
        aprendido = True
    else:
        epoca += 1
