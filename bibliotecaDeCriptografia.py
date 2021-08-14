#==========================#
#=======Encriptador========#
#==========================#

from random import *

def Encriptar(palavraInserida):


    palavra = palavraInserida
   
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*Çabcdefghijklmnopqrstuvwxyz '

    caracteres2 = ''

    n = choice(range(10,len(caracteres)))

    e = (len(caracteres)-int(n))

    for i in range(e,(len(caracteres))):
        caracteres2 = caracteres2 + caracteres[i]

    for i in range(e):
        caracteres2 = caracteres2 + caracteres[i]



    palavraCrip = ''



    for identificadorP in range(len(palavra)):
    
        for identificadorC in range(len(caracteres)):
        
            if(palavra[identificadorP] == caracteres[identificadorC]):
                
                palavraCrip = palavraCrip + caracteres2[identificadorC]
                break
            
            else:
            
                pass



    palavraCrip = palavraCrip + str(n)

    return palavraCrip


#=============================#
#=======Desencriptador========#
#=============================#

def Desencriptar(palavraInserida):
    
    palavra = palavraInserida

    palavraDesCrip = ''

    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*Çabcdefghijklmnopqrstuvwxyz '

    caracteres2 = ''

    n = int(palavra[len(palavra)-2] + palavra[len(palavra)-1])

    palavra= palavra.replace(str(n),'')

    e = (len(caracteres)-int(n))

    for i in range(e,(len(caracteres))):
        caracteres2 = caracteres2 + caracteres[i]

    for i in range(e):
        caracteres2 = caracteres2 + caracteres[i]

    for identificadorP in range(len(palavra)):
    
        for identificadorC in range(len(caracteres)):
        
            if(palavra[identificadorP] == caracteres2[identificadorC]):
                palavraDesCrip = palavraDesCrip + caracteres[identificadorC]
                break
            
            else:
                pass
    return palavraDesCrip


