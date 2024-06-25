km = float(input('Digite quantos Km o carro rodou:'))
dias = int(input('Digite a quantidade de dias que o carro foi alugado:'))
preco= (60 * dias) + (0.15 * km)
print(f'Preço total a pagar após rodar {km:.1f}Km em {dias} dias: {preco:.2f}')