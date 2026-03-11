def calcular_amplitude(dados):
    maior = dados[0]
    menor = dados[0]
    
  
    for valor in dados:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
            
 
    return maior - menor


alimentacao = [320.00, 450.00, 390.00, 510.00, 280.00, 470.00, 360.00, 420.00, 340.00, 530.00]
transporte = [150.00, 200.00, 170.00, 220.00, 120.00, 210.00, 160.00, 190.00, 140.00, 230.00]

print("Amplitude Alimentação:", calcular_amplitude(alimentacao))
print("Amplitude Transporte:", calcular_amplitude(transporte))
