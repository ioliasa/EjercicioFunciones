# num1 = int(input("Introduce un número"))
# num2 = int(input("Introduce un número"))
# num3 = int(input("Introduce un número"))
# 
# if num1 >= num2 and num1 >=num3:
#     if num2 > num3:
#         print (num3, num2,num1)
#     else:
#         print (num2, num3,num1)
# elif num2 >= num1 and num2 >=num3:  
#     if num1 > num3:
#         print (num3, num1,num2)
#     else:
#         print (num1, num3,num2)       
# else:
#     if num1 > num2:
#         print (num2, num1,num3)
#     else:
#         print (num1, num2,num3) 
from ast import Num

# listanumero = []
# listanumero.append(int(input("Introduce un número")))
#                     
# num2 = int(input("Introduce un número"))
# listanumero.append(num2)
# 
# num2 = int(input("Introduce un número"))
# listanumero.append(num2)
# 
# print(listanumero)
# print(sorted(listanumero))
# print(listanumero)
# listanumero = sorted(listanumero)
# print(listanumero)


# lista = [0,0,0,0,0]
# for i in range (5):
#     pos = int(input("Introduce en que posición quieres guardar un número (0 al 4)"))
#     num = int(input("Introduce un número"))
#     lista[pos] = num
# print(lista)  


# lista = []
# for i in range (3):
#     nombre = input("Introduce el nombre")
#     lista.append(nombre)
    
def isPrime (num):
    resultado = 1 # supongo que es primo
    if num <= 0:
        resultado = -1
    for i in range(2,num):
        if  num % i == 0:
           resultado= 0 # N es primo porque tiene un divisor

    return (resultado)

print(isPrime(11))




