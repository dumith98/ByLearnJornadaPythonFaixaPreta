
gravidade = 9.8

def calculo_tempo(altura):
    
    tempo = ((2*altura)/gravidade)**(1/2)
    print('O tempo que leva para o objeto chegar ao solo é: ', tempo, 'segundos.')

def calculo_altura(tempo):
    
 
    altura = (gravidade * pow(tempo, 2)) / 2
    print('Se o objeto cair por', tempo, 'segundos, ele teria sido largado de uma altura igual a ', altura, 'metros.')

print('Bem vindo a e obrigado por utilizar a minha calculadora de queda livre!')
print('--------------------')
print('Vale lembrar que estamos desconsiderando a resistencia do are considerando a gravidade igual a 9.8 m/s²!')
print('--------------------')


escolha = input('Escolha o que quer descobrir, altura ou tempo?: ')

 
while escolha != 'tempo' and escolha != 'altura':   
    print('Voce deve ter digitado algo errado. Tente de novo.')
    escolha = input('Escolha o que quer descobrir, altura ou tempo?: ') 
if escolha == 'tempo':
    altura = float(input('Informe a altura da qual o objeto foi largado em metros: '))    
    calculo_tempo(altura)
elif escolha == 'altura':
    tempo = float(input('Informe por quanto tempo o objeto vai cair em segundos: '))
    calculo_altura(tempo)
