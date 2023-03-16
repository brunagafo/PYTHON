print('Pintando uma parede! \nMe diga as dimensões e te direi quantos litros de tinta usar.\n')
alt = float(input('Digite o valor da altura da parede: '))
lar = float(input('Digite o valor da largura da parede: '))
ar = alt * lar
print('A área da sua parede é de {:.2f} m². Você precisa de {:.1f} litros de tinta para pintá-la.' .format(ar, (ar/2)))
