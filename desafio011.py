largura = float(input('Digite a largura da parede (Em m):'))
altura = float(input('Digite a altura da parede (Em m):'))
area = (largura * altura)
tinta = (area / 2) 
print(f'Para a pintura de uma parede com área igual a {area:.2f}m² é preciso de {tinta:.1f}L de tinta')