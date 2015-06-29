# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:46:40 2015

@author: Raphael
"""
#import random

listaopcoes=['tesoura','papel','pedra','lagarto','spock']

contador=0
contador2=0
while contador < 3 or contador2 < 3:
    
    escolha2=listaopcoes[1]
    escolha=input("Escolha um movimento:  ").lower()
    
    print("asd")

    if escolha =="tesoura": 
        if escolha2=='lagarto':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='papel':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='spock':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='pedra':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='tesoura':
            print("Opa! O outro jogador também escolheu '%s'. Deu empate!" %escolha2)
            contador=0
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
    
    elif escolha =='pedra':
        if escolha2=='tesoura':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='lagarto':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='spock':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='papel':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='pedra':
            print("Opa! O outro jogador também escolheu '%s'. Deu empate!" %escolha2)
            contador=0
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
    elif escolha =='papel':
        if escolha2.lower=='pedra':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='spock':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='tesoura':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='lagarto':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='papel':
            print("Opa! O outro jogador também escolheu '%s'. Deu empate!" %escolha2)
            contador=0
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
    elif escolha =='spock':
        if escolha2=='tesoura':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='pedra':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='lagarto':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='papel':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2.lower=='spock':
            print("Opa! O outro jogador também escolheu '%s'. Deu empate!" %escolha2)
            contador=0
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
    elif escolha =='lagarto':
        if escolha2.lower=='spock':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='papel':
            print("Opa! O outro jogador escolheu '%s'. Você ganhou!" %escolha2)
            contador+=1
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='tesoura':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='pedra':
            print("Opa! O outro jogador escolheu '%s'. Você perdeu!" %escolha2)
            contador=0
            contador2+=1
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
            
        if escolha2=='lagarto':
            print("Opa! O outro jogador também escolheu '%s'. Deu empate!" %escolha2)
            contador=0
            contador2=0
            print("PLACAR- Você: ",contador, "Outro jogador: ", contador2 )
    else:
        print("Você não digitou uma opção válida. Tente novamente.")
print("FIM DE JOGO!")    