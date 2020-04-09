# Script creado el 07/04/2020 por Xabier Gabiña ak.Xabierland
# Mi Github: https://github.com/Xabierland
# Mi Twitter: https://twitter.com/Xabierland
# Mi Instagram: https://www.instagram.com/xabierland/

# Libreias importadas

#Todo lo que escriba se transforma en 'I'
def transforma(men,minus,mayus):
    i=0
    men1= list(men)
    while i<=len(men1)-1:
        if men1[i]=='a' or men1[i]=='e' or men1[i]=='i' or men1[i]=='o' or men1[i]=='u':
            men1[i]=minus
        elif men1[i]=='A' or men1[i]=='E' or men1[i]=='I' or men1[i]=='O' or men1[i]=='U':
            men1[i]=mayus
        
        i=i+1
    escribir(men1)

def minusymayus(vocal):
    minus=''
    mayus=''
    if vocal=='a' or vocal=='A':
        minus='a'
        mayus='A'
    if vocal=='e' or vocal=='E':
        minus='e'
        mayus='E'
    if vocal=='i' or vocal=='I':
        minus='i'
        mayus='I'
    if vocal=='o' or vocal=='o':
        minus='o'
        mayus='O'
    if vocal=='u' or vocal=='U':
        minus='u'
        mayus='U'
    else:
        print("Error al introducir la vocal")
        print("Abortanto programa")
        raise SystemExit
    return(minus, mayus)

#Resetea en caso de que asi se desee para que se pueda introducir otra frase.
def reset():
    print("Escribe Y (Yes) para repetir o pulsa cualquier otra tecla para salir")
    select2=input()
    if select2=='Y' or select2=='y' or select2=="Yes" or select2=="yes":
        print("Introduce un nuevo mensaje por teclado")
        main()
    else:
        print("Abortando programa")
        raise SystemExit

def escribir(men):
    men="".join(men)
    print("El mensaje resultante de la transformacion es:")
    print("=====================================================================================================================================================================")
    print (men)
    print("=====================================================================================================================================================================")

#Programa principal y encargado de llamar al resto de funciones
def main(minus,mayus):
    men=input()
    print(f"Tu mensaje a transformar es: =>  {men}  <= ?")
    print("Escribe Y/N (Yes/No) para continuar o pulsa cualquier otra tecla para salir")
    select1=input()
    if select1=='Y' or select1=='y' or select1=="Yes" or select1=="yes":
        transforma(men,minus,mayus)
        reset()
    elif select1=='N' or select1=='n' or select1=="No" or select1=="no":
        print("Introduce el mensaje correcto por teclado")
        main()
    else:
        print("Abortando programa")

#Inicio  
print("Introduce la vocal por la que quieres transformar el resto")
vocal=''
vocal=input()  
minus,mayus=minusymayus(vocal)
print("Introduce un mensaje por teclado")
men=""
main(minus,mayus)

#===========================================================================================================#
# Version 1.0 | Rediseño mejorado del proyecto https://github.com/Xabierland/Todas-las-vocales-a-i
# Eres libre de editar y distribuir este codigo como te plazca sin necesidad de dar credito a mi, su autor.