a=int(input("Introduce el primer numero "))
b=int(input("Introduce el segundo numero "))
for i in range(a,b):
    if(i%2==0):
        print("El numero ",i,"es par")
    else:
        print("El numero",i,"es impar")
