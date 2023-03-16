n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
di = n1 // n2
p = n1 ** n2
rd = n1 % n2
print('A soma é {}, a multiplicação é {}, a divisão é {:.2f}, a subtração é {}' .format(s, m, d, sub), end='')
print('A divisão inteira é {}, a potência é {}, o resto da divisão é {}.' .format(di, p, rd))


