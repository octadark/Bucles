
#Básico: imprime todos los números enteros del 0 al 150
for num in range (0,151):
    print(num)
print('--')


#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
for num in range (5,1001,5):
    print(num)
print('---')

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for num in range(101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else: print (num)
print('----')

#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
impares = 0
for num in range(1, 500001, 2):
    impares += num
    print(impares)
print('-----')

#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for num in range(2018,0,-4):
    print(num)
print('------')
#Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 
low = 2
high = 9
mult = 3
for num in range(low,high + 1):
    if num % mult == 0:
        print(num)
print('------')