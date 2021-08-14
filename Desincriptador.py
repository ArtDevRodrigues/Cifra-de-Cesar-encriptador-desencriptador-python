#Crifra de Cesar

palavra = input('Insira a palavra que vai ser Descriptografada: ')
print('=====================================')

palavraDesCrip = ''
#palavraDesCrip2 = ''


caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*Çabcdefghijklmnopqrstuvwxyz '

caracteres2 = ''

n = int(palavra[len(palavra)-2] + palavra[len(palavra)-1])

palavra= palavra.replace(str(n),'')

e = (len(caracteres)-int(n))
'''
print(' local da letra de comeco: ',e)

print(' numero de caracteres: ',len(caracteres))
'''
for i in range(e,(len(caracteres))):
    caracteres2 = caracteres2 + caracteres[i]

for i in range(e):
    caracteres2 = caracteres2 + caracteres[i]

for identificadorP in range(len(palavra)):
    
    for identificadorC in range(len(caracteres)):
        
        if(palavra[identificadorP] == caracteres2[identificadorC]):
            
            palavraDesCrip = palavraDesCrip + caracteres[identificadorC]
            #palavraDesCrip2 = palavraDesCrip2 + caracteres[identificadorC] + ' \ '
            break
            
        else:
            #print('Letra não correspondente. ', identificadorC)
            pass



print('Palavra Descriptografada :  ',palavraDesCrip)
print('Palavra Descriptografada :  ',palavraDesCrip2)

