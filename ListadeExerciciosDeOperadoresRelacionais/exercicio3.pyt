granja = float(input("Digite o numero de galinhas da granja: "))

chip_pe_Esquerdo = 0.35 *2
chip_pe_Direito = 0.40
gasto_por_galinha = chip_pe_Direito + chip_pe_Esquerdo
gasto_granja = gasto_por_galinha * granja

print(f'O gasto de sua granja é: {gasto_granja} ')