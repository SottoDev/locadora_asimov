from data import dados

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