'''
Função para verificar se o movimento do cavalo é válido. 
Ela analisa se as posições iniciais e finais estão dentro dos limites do tabuleiro: 
    Caso não estejam, retorna um erro;
Caso estejam, calcula as diferenças nas colunas e linhas e determina se o movimento é válido para um cavalo, seguindo as duas regras de movimento:
    i) Caso o cavalo "ande duas colunas" para quaisquer uma das duas direções, deve se mover uma linha, para cima ou para baixo, na coluna resultante (L)
    i) Caso o cavalo ande para uma das duas colunas adjacentes, deve andar apenas uma linha, para cima ou para baixo, na coluna resultante (L).
O programa roda, reclamando de inputs errados, até que o usuário digite como entrada a letra 'f'.
'''

def checaMovimento(inicial,final):
    colunas = ['a','b','c','d','e','f','g','h']
    linhas = ['1','2','3','4','5','6','7','8']
    if inicial[0] not in colunas or inicial[1] not in linhas or final[0] not in colunas or final[1] not in linhas:
        return "Erro. Input inválido."
    deslocamentoLinhas = abs(colunas.index(inicial[0]) - colunas.index(final[0]))
    deslocamentoColunas = abs(linhas.index(inicial[1])- linhas.index(final[1]))
    if (deslocamentoLinhas == 1 and deslocamentoColunas == 2) or (deslocamentoLinhas == 2 and deslocamentoColunas == 1):
        return "VÁLIDO"
    else:
        return "INVÁLIDO"
    
while(1):
    movimento = input()
    if movimento  == 'f':
        break
    inicial, final = movimento.split(' ')
    print(checaMovimento(inicial,final))

print("Fim...")