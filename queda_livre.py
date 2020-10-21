
gravidade = 9.8
opcoes = ['tempo', 'altura', 'teoria']
def calculo_tempo(altura):
    
    tempo = ((2*altura)/gravidade)**(1/2)
    print(f'O tempo que leva para o objeto chegar ao solo é: {tempo} segundos.')

def calculo_altura(tempo):
    

    altura = (gravidade * pow(tempo, 2)) / 2
    print(f'Se o objeto cair por {tempo} segundos, ele teria sido largado de uma altura igual a {altura} metros.')

print('Bem vindo a e obrigado por utilizar a minha calculadora de queda livre!')
print('--------------------')
print('Vale lembrar que estamos desconsiderando a resistencia do are considerando a gravidade igual a 9.8 m/s²!')
print('--------------------')


escolha = input('Escolha o que quer descobrir: altura, tempo ou teoria?: ')

 
if escolha in opcoes:
    if escolha == 'tempo':
        altura = float(input('Informe a altura da qual o objeto foi largado em metros: '))    
        calculo_tempo(altura)
    elif escolha == 'altura':
        tempo = float(input('Informe por quanto tempo o objeto vai cair em segundos: '))
        calculo_altura(tempo)
    elif escolha == 'teoria':
        print('pera que ja estou escrevendo isso!')
else:
    print('Voce deve ter digitado algo errado. Tente de novo.')
    escolha = input('Escolha o que quer descobrir, altura ou tempo?: ') 

    