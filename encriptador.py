#Crifra de Cesar

from random import *
#n = input('Numero: ')
n = choice(range(2,26))
#n = 10
print(n)

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*Çabcdefghijklmnopqrstuvwxyz '

caracteres2 = ''

e = (len(caracteres)-int(n))
'''
print(' local da letra de comeco: ',e)

print(' numero de caracteres: ',len(caracteres))
'''
for i in range(e,(len(caracteres))):
    caracteres2 = caracteres2 + caracteres[i]

for i in range(e):
    caracteres2 = caracteres2 + caracteres[i]

print('=====================================')
palavra = input('Insira a palavra que vai ser criptografia: ')
print('=====================================')

palavraCrip = ''
palavraCrip2 = ''

#x = int((len(palavra)/2)-0.5)

for identificadorP in range(len(palavra)):
    
    '''if(identificadorP == x+1):
        palavraCrip = palavraCrip + str(n) + ' \ '
    '''

    for identificadorC in range(len(caracteres)):
        
        if(palavra[identificadorP] == caracteres[identificadorC]):
            
            palavraCrip = palavraCrip + caracteres2[identificadorC]
            palavraCrip2 = palavraCrip2 + caracteres2[identificadorC] + ' \ '
            break
            
        else:
            #print('Letra não correspondente. ', identificadorC)
            pass



palavraCrip = palavraCrip + str(n)

print('Palavra criptografada :  ',palavraCrip2)
print('Palavra criptografada :  ',palavraCrip)


        



        


