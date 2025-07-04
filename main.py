import time
from data import dados


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

for i in range(len(modelos)):
    modelo = modelos[i]
    diaria = dados.carros[categoria_escolhida][modelo]
    print(f"{i} - {modelo} - R${diaria:.2f} / dia")

escolha_modelo = int(input("Escolha uma categoria: "))
    
    
dias_de_viagem = int(input(f"Agora me diga, quantos dias pretende ficar com o {modelo} ? "))

total_de_custo = dias_de_viagem*diaria

print(f"O custo total será de R$ {total_de_custo}")

print("Carro sendo reservado...")
carregando()
print(f"Carro reservado com sucesso, venha buscar dia")# colocar 3d apos a data atual

#aprovacao = 
## Colocar aprovação, colocar se aceita ou não, colocar um dia ficctio pra pegar, retirar os carros ja selcionas - a locadora do pai ainda ta fraquinha-