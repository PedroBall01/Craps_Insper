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

# Aposta do 'Pass Line Bet'
while fichas > 0:
    print("Voce tem {0} fichas".format(fichas))
    print("Voce pode apostar em: ")
    print("Pass Line Bet")
    # coloca aqui a proxima aposta
    print("Pare (Se não quiser apostar mais)")
    opcao = input("Em qual voce quer apostar: ")
    if opcao == "Pass Line Bet":
        aposta = int(input("Quanto quer apostar?: "))
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
    # inicio do cofigo da nova aposta
    elif opcao == "Pare":
        print("Voce parou com {0} fichas".format(fichas))
        break
if fichas <= 0:
    print("Acabaram suas fichas!")
    

#Pass Line Bet

#Teste github
