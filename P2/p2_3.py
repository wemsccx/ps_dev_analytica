'''
Função para calcular o troco de um usuário.
Recebe um valor em reais e calcula a (menor) distribuição de notas e moedas para representar esse valor.
Ela percorre duas listas, ordenadas de forma decrescente:uma para as notas e outra para as moedas 
A cada iteração o valor que o usuário digitou é dividido e subtraido (através da função módulo)pelos elementos das listas, para calcular a (menor) quantidade de cada uma das notas e moedas.
Ao fim, exibe a quantidade de cada uma delas.
O programa roda apenas uma única vez, e avisa ao usuário caso a entrada seja inválida.
'''

def troco(valor):
    notas = [100,50,20,10,5,2]
    moedas = [1.00,0.5,0.25,0.10,0.05,0.01]
    print(f'NOTAS:')
    for i in notas:
        print(f'{int(valor/i)} nota(s) de R${i}.00')
        valor %= i
    print(f'MOEDAS:')
    for i in moedas:
        print(f'{int(valor/i)} moedas de R${i:.2f}')
        valor %= i

valor = input()
try:
    valor = float(valor) # Vê se o valor do usuário realmente é um número (aceita reais e inteiros, positivos, nulos e negativos) 
except ValueError:
    print("Erro. Input inválido.")
else:
    if valor >= 0:
        troco(valor) # Vê se o valor do usuário é não-negativo (representa um valor monetário)
    else:
        print ("Erro. Insira apenas números positivos.")

