def fibonacci(n):
  if n < 0:
    return None

  if n == 0:
    return 0
  elif n == 1:
    return 1

  return fibonacci(n - 1) + fibonacci(n - 2)


while True:
  try:
    user_inp = int(input('Enter the no. of fibonacci series: '))
    print(fibonacci(user_inp))
    break
  except:
    print('Please print a valid value....')
