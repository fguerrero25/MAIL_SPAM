filename= open('/texto1.txt')
file=filename.read()
filename.close()
dividir= file.split()#Convierto a lista para poder interar
alfabeto = ("abcdefghijkmnopqrstumnxz")

#Test purposes
# print(file)  
# print(dividir)

print(len(dividir)) 

hostname = input('HOSTNAME  :')
for letra in alfabeto: #POR CADA LETRA EN ALFABETO
    for letr in dividir:#POR CADA LINEA EN DIVIDIR 
        f = open("/texto.txt", "a") 
        print(letra + letr + hostname, file=f)
        f.close()
        
print("Verifica el txt llamado texto en la raiz")
