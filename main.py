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
    
def calcular_multa_autoestrada(velocidade):
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

def main():
    while True:    
        opcao = menu()
        if opcao == '4':
            print("Programa encerrado.")
            break

        velocidade = float(input("Digite a velocidade do veículo"))


        if opcao == '1':
            multa = calcular_multa_localidade(velocidade)
        elif opcao == '2':
            multa = calcular_multa_fora_localidade(velocidade)
        elif opcao == '3':
            multa = calcular_multa_autoestrada(velocidade)
        else:
            print("Opção Inválida")
            continue

        if multa == 0:
            print("Sem multa. Condução dentro do limite.")
        else:
            print(f"Multa a pagar: {multa} $")

if __name__ == "__main__":
    main()