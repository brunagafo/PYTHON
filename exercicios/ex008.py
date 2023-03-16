print('Digite um valor em metros e eu converterei para cm e mm!')
n = float(input('Quantos metros você gostaria de converter? '))
cm = n * 100
mm = n * 1000
print('\nO valor convertido é {:.0f}cm e {:.0f}mm.' .format(cm, mm))
