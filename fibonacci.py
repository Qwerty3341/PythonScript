end_of_sequence = int(input('Enter the end to the secuence: '))

def fibonacci(num):
  a , b = 0 , 1
  for i in range(num):
    yield a
    container = a
    a = b
    b = container + b

for x in fibonacci(end_of_sequence):
  print(x)