import time
from data import dados
import os

while True:
    
    def limpar_console():
        os.system('cls' if os.name=="nt" else "clear")
    
    
    def carregando():
        for _ in range (3):
            time.sleep(0.5)
            print(".", end ="", flush=True)
        time.sleep(0.5)
        print()


    categoria = list(dados.carros.keys())

    print("="*30)
    print("Bem vindo a locadora")
    print("="*30)
    print("Primeiro vamos escolher o categoria")

    for i in range(len (categoria)):
        print(i,"-",categoria[i])   
      
    escolher_categoria= int(input("Digite o numero da categoria escolhida: "))
    categoria_escolhida = categoria[escolher_categoria]

    modelos = list(dados.carros[categoria_escolhida].keys())
    limpar_console()
    
    for i in range(len(modelos)):
        modelo = modelos[i]
        diaria = dados.carros[categoria_escolhida][modelo]
        print(f"{i} - {modelo} - R${diaria:.2f} / dia")

    escolha_modelo = int(input("Escolha uma categoria: "))
    modelo_escolhido = modelos[escolha_modelo]
    diaria = dados.carros[categoria_escolhida].pop(modelo_escolhido)
    limpar_console()
            
          
            
    dias_de_viagem = int(input(f"Agora me diga, quantos dias pretende ficar com o {modelo} ? "))
    total_de_custo = dias_de_viagem*diaria

    print(f"O custo total será de R$ {total_de_custo}")
    print("Verificando carro..")
    carregando()
    print(f"Carro verificado com sucesso")

    aprovacao = input("Orçamento aprovado?(S/N)").upper()

    if aprovacao == "N":
        print("Ok, reiniciando as escolhas")
        #dados.carros[categoria_escolhida][modelo_escolhido] = diaria
        carregando()
        continue
    
    elif aprovacao =="S":
        print("="*30)
        print("Carro sendo reservado")
        print("="*30)
        carregando()
        print("Carro Reservado com SUCESSO.")
        break

    ## Colocar aprovação, colocar se aceita ou não, colocar um dia ficctio pra pegar, retirar os carros ja selcionas - a locadora do pai ainda ta fraquinha-