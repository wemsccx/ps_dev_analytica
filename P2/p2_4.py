'''
Código para calcular a frequência de números inteiros com o uso de dicionários. 
Primeiro o programa checa se o número é de fato inteiro através do tratamento de exceção;
Caso seja, vemos se o número não está no nosso dicionário:
    i) Se não estiver, adicionamos essa chave com valor = 1 (primeira aparição)
    ii) Caso contrário, isto é, caso esteja no dicionáro, adicionamos ao valor da chave daquele número +1 unidade.
Ao fim, é mostrado de forma crescente todos os números com o seu respectivo número de aparições.
O programa roda, ignorando inputs inválidos, até que o usuário digite como entrada a letra 'f'.
'''

dict = {}
while(1):
    num = input()
    if num == 'f':
        break
    try:
        num = int(num) # Vê se o valor do usuário realmente é um número (aceita inteiros, positivos, nulos e negativos) 
    except ValueError:
        continue
    else:
        if num not in dict:
            dict[num] = 1
            continue
        dict[num] += 1
for i,j in sorted(dict.items()):
    str = (f'O número {i} apareceu {j} vez')
    if j > 1:
        str += 'es'
    print(str)
print("Fim...")