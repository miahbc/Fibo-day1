def fibonacci(n):
  flist = [0,1]
  if n == 0:
    return 0
  else:
    while (n>1):
  # for num in flist:
  #   # length = len(flist)
      newnum = flist[-2] + flist[-1]
      flist.append(newnum)
      n = n-1
  return int(flist[-1])


# print(fibonacci(0))
# print(fibonacci(2))
# print(fibonacci(5) == 5)
# print(fibonacci(8) == 21)
# print(fibonacci(11) == 89)
# print(fibonacci(14) == 377)
# print(fibonacci(17) == 1597)
# print(fibonacci(20) == 6765)

# print(fibonacci(0) == 0)
# print(fibonacci(2) == 1)
# print(fibonacci(5) == 5)
# print(fibonacci(8) == 21)
# print(fibonacci(11) == 89)
# print(fibonacci(14) == 377)
# print(fibonacci(17) == 1597)
# print(fibonacci(20) == 6765)
