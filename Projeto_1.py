# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:23:29 2020

@author: pedro
"""

import random
dado_1 = random.randint(1,6)
dado_2 = random.randint(1,6)
lancamento = dado_1 + dado_2

fichas = 10
# Estas sao as funcoes das apostas que nao sei como colocar no meio do codigo
""" # Aposta - Any Craps
def any_craps():
    if lancamento == 2 or lancamento == 3 or lancamento == 12:
        fichas = fichas + 7*(aposta)
    else:
        fichas=fichas-aposta

#Aposta - Twelve
def twelve():
    if lancamento == 12:
        fichas = fichas + 30*aposta
    else:
        fichas = fichas - aposta

#Aposta - Field
def field():
    if lancamento == 5 or lancamento == 6 or lancamento == 7 or lancamento == 8:
        fichas=fichas-aposta
    elif lancamento == 2:
        fichas=fichas+2*aposta
    elif lancamento ==12:
        fichas=fichas+3*aposta
    else:
        fichas=fichas+aposta  """
# Aposta do 'Pass Line Bet'
while fichas > 0:
    print("Voce tem {0} fichas".format(fichas))
    print("Voce pode apostar em: ")
    print("Pass Line Bet")
    print("Field")
    print("Any Craps")
    print("Twelve")
    # coloca aqui a proxima aposta
    print("Pare (Se não quiser apostar mais)")
    opcao = input("Em qual voce quer apostar: ")
    if opcao == "Pass Line Bet":
        aposta = int(input("Quanto quer apostar?: "))
        print("dado 1: {}".format(dado_1))
        print("dado 2: {}".format(dado_2))
        if lancamento == 7 or lancamento == 11:  # Inicio do 'Come Out'
            fichas = fichas + aposta
        elif lancamento == 2 or lancamento == 3 or lancamento == 12:
            fichas = fichas - aposta
        elif lancamento == 4 or lancamento == 5 or lancamento == 6 or lancamento == 8 or lancamento == 9 or lancamento == 10: # Inicio do 'Point'
            i = True
            while i:
                dado_3 = random.randint(1,6)
                dado_4 = random.randint(1,6)
                lancamento_novo = dado_3 + dado_4
                if lancamento_novo == lancamento or lancamento_novo == 7:
                    i = False
            if lancamento_novo == lancamento:
                fichas = fichas + aposta
            elif lancamento_novo == 7:
                fichas = fichas - aposta
    # Aposta - Twelve
    elif opcao == "Twelve":
        aposta = int(input("Quanto quer apostar? "))
        if lancamento == 12:
            fichas = fichas + 30*aposta
        else:
            fichas = fichas - aposta
    # Aposta - Field
    elif opcao == "Field":
        if lancamento == 5 or lancamento == 6 or lancamento == 7 or lancamento == 8:
            fichas=fichas-aposta
        elif lancamento == 2:
            fichas=fichas+2*aposta
        elif lancamento ==12:
            fichas=fichas+3*aposta
        else:
            fichas=fichas+aposta
    # Aposta - Any Craps
    elif opcao == "Any Craps":
        if lancamento == 2 or lancamento == 3 or lancamento == 12:
            fichas = fichas + 7*(aposta)
        else:
            fichas=fichas-aposta
    #Parando
    elif opcao == "Pare":
        print("Voce parou com {0} fichas".format(fichas))
        break
if fichas <= 0:
    print("Acabaram suas fichas!")
    

#Pass Line Bet