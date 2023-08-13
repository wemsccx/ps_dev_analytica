'''
Função utilizada para ver se o input do usuário está no formato válido.
'''

def valida(horario):
    if len(horario) != 5: # O formato 'hh:mm' tem exatamente 5 caracteres
        return False
    horas, minutos = horario.split(':')
    try: # Apenas passa daqui se ambas as partes do input do usuário são inteiros (aceita positivos, negativos e nulos)
        horas = int(horas)
        minutos = int(minutos)
    except ValueError:
        return False
    else:
       # Confirma se o input do usuário está dentro do intervalo do formato 24h e de quebra exclui os números negativos.
       if (0 <= horas <= 23) and (0 <= minutos <= 59): 
           return True
       
'''
Função que calcula o menor ângulo levando em conta que o ponteiro de horas apenas se move quando a hora é realmente completada.
A expressão utilizada para o cálculo foi obtida expandindo a fórmula |(360/60) * m - (360/12) * h|
'''

def menorAngulo(horario):
    horas, minutos = horario.split(':')
    horas, minutos = int(horas),int(minutos)
    horas %= 12
    angulo = abs((minutos*6)-(horas*30))
    return min(angulo,360-angulo)

while (1):
    horario = input()
    if horario  == 'f':
        break
    if valida(horario):
        print(f'O menor ângulo é de {menorAngulo(horario)}º')
    else:
        print("Input inválido")
print("Fim...")
