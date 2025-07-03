def calcular_multa_localidade(velocidade):
    if velocidade <= 50:
        return 0
    elif velocidade < 90:
        return 60
    elif velocidade < 90:
        return 120
    else:
        return 320
    
def calcular_multa_fora_localidade(velocidade):
    if velocidade <= 90:
        return 0 
    elif velocidade < 120:
        return 60
    else:
        return 120
    

