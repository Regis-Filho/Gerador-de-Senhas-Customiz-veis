from os import system
from random import randint
from random import choice



def cabecalho():
    system('cls')
    print("|"+ 'GERADOR DE SENHAS'.center(60) +"|")
    print('-'*62)


def inicio():
    global escolha_us 
    try:
        print("|"+ '1.QUANTIDADE DE CARACTERES.'.ljust(60)  +"|")
        print("|"+ '2.DEFINIR COMPONENTES.'.ljust(60)  +"|")
        print("|"+ '3.GERAR A SENHA.'.ljust(60)  +"|")
        print('-'*62)
        escolha_us = int(input('DIGITE O NUMERO REFERENTE: '))
        system("cls")
        


    except ValueError:
        system("cls")
        cabecalho()
        print("|"+ 'DIGITE APENAS NUMEROS.'.ljust(60)  +"|")
        input("|"+ 'ENTER PARA CONTINUAR.'.ljust(60)  +"|")
    

def caracteres():
    global qtd_caracteres
    qtd_caracteres = int(input('DIGITE A QUANTIDADE DE CARACTERES : '))
    


def componentes():
    global letras_M,letras_m,numeros,simbolos
    letras_M = input("DESEJA TER LETRAS MAIÚSCULAS ? S/N ").upper()
    print('-'*62)
    letras_m = input("DESEJA TER LETRAS MINÚSCULAS ? S/N ").upper()
    print('-'*62)
    numeros = input("DESEJA TER NÚMEROS ? S/N ").upper()
    print('-'*62)
    simbolos = input("DESEJA TER SÍMBOLOS ? S/N ").upper()








def gerar_senha():
    global senha
    senha = ''
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caracteres_especiais = ['!', '@', '#', '$', '%','&','*']
    
    contador = 0
    while not contador == qtd_caracteres:
        try:
            if letras_M == "S":
                senha += choice(alfabeto).upper()
                contador+=1
                if contador == qtd_caracteres:
                    break
            if letras_m == "S":
                senha += choice(alfabeto)
                contador+=1
                if contador == qtd_caracteres:
                    break
            if numeros == "S":
                senha += str(randint(0,9))
                contador+=1
                if contador == qtd_caracteres:
                    break
            if simbolos == "S":
                senha += choice(caracteres_especiais)
                contador+=1
                if contador == qtd_caracteres:
                    break
            senha_gerada=True
        except:
            senha_gerada = False


    if senha_gerada:
        print("|"+ 'SENHA GERADA COM SUCESSO :'.ljust(60)  +"|")
        print("|"+ senha.ljust(60)  +"|")
        input("|"+ 'ENTER PARA CONTINUAR.'.ljust(60)  +"|")

    











while True:
    cabecalho()
    inicio()
    cabecalho()
    match escolha_us:
        case 1:
            caracteres()
        case 2:
            componentes()
        case 3:
            gerar_senha()
        case _:
            print('INVÁLIDO')

    
            










    