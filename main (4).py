y = 0
x = int(input('First Number: '))
divisor = int(input('Second Number: '))
while x >= divisor:
  x -= divisor
  y += 1

print(f'Quotient: {y} & remainder {x}')