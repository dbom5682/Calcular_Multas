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
    
def calcular_multa_autoestraa(velocidade):
    if velocidade <= 120:
        return 0
    elif velocidade <= 150:
        return 60
    elif velocidade <= 175:
        return 120
    else: 
        return 360
    
def menu():
    print("\n=== MENU DAS MULTAS DE CIRCULAÇÃO ===")
    print("1 - Localidade")
    print("2 - Fora da Localidade")
    print("3 - Autoestrada")
    print("4 - Sair")
    return input("Escolha uma opção")