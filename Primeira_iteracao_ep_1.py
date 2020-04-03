# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:40:25 2020

@author: pedro
"""

import random

fichas = 100


while fichas > 0:
   
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    lancamento = dado_1 + dado_2
   
    print("Voce tem {0} fichas".format(fichas)) 
    print("Voce esta na fase de 'Come Out' !")
    print("Voce pode apostar em: ")    
    print("Pass Line Bet")
    print("Field")
    print("Any Craps")
    print("Twelve")
    print("Pare (Se não quiser apostar mais)")
   
    # Inicio do 'Come Out'
    opcao = input("Em qual voce quer apostar: ")
   
    # Aposta do 'Pass Line Bet' no Come Out
    if opcao == "Pass Line Bet": 
        aposta = int(input("Quanto quer apostar?: "))
        print("dado 1: {}".format(dado_1))
        print("dado 2: {}".format(dado_2))
        if lancamento == 7 or lancamento == 11: 
            fichas = fichas + aposta
        elif lancamento == 2 or lancamento == 3 or lancamento == 12:
            fichas = fichas - aposta
       
        # Inicio do 'Point'      
        else:
            dado_novo_1 = random.randint(1,6)
            dado_novo_2 = random.randint(1,6)
            lancamento_soma_dados = dado_novo_1 + dado_novo_2
            print("Voce entrou na fase de 'Point' !")
            print("Voce pode continuar no 'Pass Line Bet' (Digite: 'continuar')")
            print("Voce pode apostar no 'Field' ")
            print("Voce pode apostar no 'Any Craps' ")
            print("Voce pode apostar no 'Twelve' ")
            opcao_nova = input("Em qual voce quer apostar: ")
            
            # Continuação do Pass Line Bet         
            if opcao_nova == "continuar":
                re_aposta = int(input("Quanto quer apostar agora? : "))
                i = True
                while i:
                    dado_em_repeticao_1 = random.randint(1,6)
                    dado_em_repeticao_2 = random.randint(1,6)
                    lancamento_novo = dado_em_repeticao_1 + dado_em_repeticao_2
                    if lancamento_novo == lancamento or lancamento_novo == 7:
                        i = False
                if lancamento_novo == lancamento:
                    fichas = fichas + re_aposta
                elif lancamento_novo == 7:
                    fichas = fichas - re_aposta
           
            # Aposta 'Field' no Point         
            elif opcao_nova == "Field":
                re_aposta = int(input("Quanto quer apostar agora? : "))
                print("dado 1: {}".format(dado_novo_1))
                print("dado 2: {}".format(dado_novo_2))
                if lancamento_soma_dados == 5 or lancamento_soma_dados == 6 or lancamento_soma_dados == 7 or lancamento_soma_dados == 8:
                    fichas = fichas - re_aposta
                elif lancamento_soma_dados == 2:
                    fichas = fichas + 2*re_aposta
                elif lancamento_soma_dados == 12:
                    fichas = fichas + 3*re_aposta
                else:
                    fichas = fichas + re_aposta
           
            # Aposta 'Any Craps' no Point
            elif opcao_nova == "Any Craps":
                re_aposta = int(input("Quanto quer apostar agora? : "))
                print("dado 1: {}".format(dado_novo_1))
                print("dado 2: {}".format(dado_novo_2))
                if lancamento == 2 or lancamento == 3 or lancamento == 12:
                    fichas = fichas + 7*(re_aposta)
                else:
                    fichas = fichas - re_aposta
            # Aposta 'Twelve' no Point
           
            elif opcao_nova == "Twelve":
                re_aposta = int(input("Quanto quer apostar agora? : "))
                print("dado 1: {}".format(dado_novo_1))
                print("dado 2: {}".format(dado_novo_2))
                if lancamento == 12:
                    fichas = fichas + 30*re_aposta
                else:
                    fichas = fichas - re_aposta
   
    # Aposta - Twelve no Come Out 
    elif opcao == "Twelve":
        aposta = int(input("Quanto quer apostar? "))
        print("dado 1: {}".format(dado_1))
        print("dado 2: {}".format(dado_2))
        if lancamento == 12:
            fichas = fichas + 30*aposta
        else:
            fichas = fichas - aposta
    
    # Aposta - Field no Come Out
    elif opcao == "Field":
        aposta = int(input("Quanto quer apostar? "))
        print("dado 1: {}".format(dado_1))
        print("dado 2: {}".format(dado_2))
        if lancamento == 5 or lancamento == 6 or lancamento == 7 or lancamento == 8:
            fichas = fichas - aposta
        elif lancamento == 2:
            fichas = fichas + 2*aposta
        elif lancamento == 12:
            fichas = fichas + 3*aposta
        else:
            fichas = fichas + aposta
    
    # Aposta - Any Craps no Come Out
    elif opcao == "Any Craps":
        aposta = int(input("Quanto quer apostar? "))
        print("dado 1: {}".format(dado_1))
        print("dado 2: {}".format(dado_2))
        if lancamento == 2 or lancamento == 3 or lancamento == 12:
            fichas = fichas + 7*(aposta)
        else:
            fichas = fichas - aposta
   
    #Parando
    elif opcao == "Pare":
        print("Voce parou com {0} fichas".format(fichas))
        break

# Filtro de saida
if fichas <= 0:
    print("Acabaram suas fichas :( ")
    




































